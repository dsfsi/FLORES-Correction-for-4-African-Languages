import os
import sys
import glob
import evaluate
from tabulate import tabulate
from nltk import word_tokenize
from comet import download_model

def find_ckpt_files(directory):
  ckpt_files = glob.glob(f"{directory}/**/*.ckpt", recursive=True)
  return ckpt_files[0] if ckpt_files else None

def get_comet_model_path():
  directory = '../comet_model'
  if not os.path.exists(directory):
    model_path = download_model('masakhane/africomet-mtl', directory)
  else:
    model_path = find_ckpt_files(directory)
    if not model_path:
      sys.exit(f'Model checkpoint not found. Delete the "{model_path}" directory and run this file again.')
  return model_path

def get_different_sentences(lines1, lines2):
  diff_sents = []

  if len(lines1) != len(lines2):
    raise ValueError(f"Files have different number of lines! {len(lines1)}, {len(lines2)}")

  for sent1, sent2 in zip(lines1, lines2):
    if sent1 != sent2:
      diff_sents.append([sent1, sent2])

  return diff_sents

def compute_token_divergence(sents1, sents2):
  differing_tokens = 0
  total_tokens = 0
  for sent1, sent2 in zip(sents1, sents2):
    tokens_zulu = word_tokenize(sent1)
    tokens_corrected = word_tokenize(sent2)

    differing_tokens += sum(1 for token in tokens_zulu if token not in tokens_corrected) + \
                        sum(1 for token in tokens_corrected if token not in tokens_zulu)

    total_tokens += len(set(tokens_zulu).union(set(tokens_corrected)))

  if total_tokens == 0:
    return 0
  else:
    return round(differing_tokens / total_tokens * 100, 1)

def compute_token_counts(sents):
  return sum(len(word_tokenize(sent)) for sent in sents)

def compute_metrics(src, ref, pred, model):
  bleu = evaluate.load("bleu")
  ter = evaluate.load('ter')

  references = [[l] for l in ref]
  predictions = pred

  data = [{'src': s, 'mt': m, 'ref': r} for s, m, r in zip(src, ref, pred)]
  model_output = model.predict(data, batch_size=8, gpus=1)

  bleu_score = bleu.compute(predictions=predictions, references=references)['bleu']
  ter_score = ter.compute(predictions=predictions, references=references)
  comet_score = model_output.system_score

  return bleu_score, ter_score, comet_score

def display_results(lang, split, corrected_sentences, src, pred, ref, bleu_score, ter_score, comet_score):
  tkcnto = compute_token_counts(pred)
  tkcntc = compute_token_counts(ref)
  data = [
    ["Language", lang],
    ["Split", split],
    ["Number of corrected sentences", f"{len(corrected_sentences)} ({len(corrected_sentences) / len(src) * 100:.1f}%)"],
    ["Token counts in original data", f"{tkcnto:,}"],
    ["Token counts in corrected data", f"{tkcntc:,}"],
    ["Token difference", f"{abs(tkcnto - tkcntc):,}"],
    ["Token divergence", f"{compute_token_divergence(ref, pred)}%"],
    ["TER", f'{ter_score["score"]:.1f}'],
    ["TER #edits", f"{ter_score['num_edits']:,}"],
    ["BLEU", f'{(bleu_score * 100):.1f}'],
    ["COMET score", f'{(comet_score * 100):.1f}']
  ]
  
  print(tabulate(data, headers=["Metric", "Value"], tablefmt="pretty", colalign=("left", "left")))