import evaluate

from nltk import word_tokenize

bleu = evaluate.load("bleu")
ter = evaluate.load('ter')

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
  references = [[l] for l in ref]
  predictions = pred

  data = [{'src': s, 'mt': m, 'ref': r} for s, m, r in zip(src, ref, pred)]
  model_output = model.predict(data, batch_size=8, gpus=1)

  bleu_score = bleu.compute(predictions=predictions, references=references)['bleu']
  ter_score = ter.compute(predictions=predictions, references=references)
  comet_score = model_output.system_score

  return bleu_score, ter_score, comet_score