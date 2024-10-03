# FLORES Dataset Corrections for Four African Languages

This project focuses on correcting the FLORES evaluation dataset (dev and devtest) for four African languages: **Hausa**, **Northern Sotho (Sepedi)**, **Xitsonga**, and **isiZulu**. The original dataset, though groundbreaking in covering low-resource languages, contained several inconsistencies and inaccuracies in these languages, which could affect the quality of evaluations in Natural Language Processing (NLP) tasks, especially for machine translation.

## Overview

In this project, native speakers meticulously reviewed and corrected the dataset to ensure improved accuracy and reliability for each language. Our goal was to enhance the integrity of downstream NLP tasks that use this data.

### Key Corrections:
- **Hausa**
- **Northern Sotho (Sepedi)**
- **Xitsonga**
- **isiZulu**

### What We Did:
1. **Reviewed and Corrected Errors**: Identified and implemented corrections to translation inconsistencies and inaccuracies in the dataset.
2. **Statistical Analysis**: Conducted statistical comparisons between the original and corrected datasets, highlighting the differences and improvements made.
3. **Improved Dataset Quality**: Enhanced linguistic accuracy and reliability, ensuring more effective evaluation of NLP tasks involving these languages.

### Evaluating the Corrections:

| lang         | # corr. (\%) | # tokens$_o$ | # tokens$_c$ | $\Delta$ tokens | % div. | # corr. (\%) | \# tokens$_o$ | \# tokens$_c$ | $\Delta$ tokens | \% div. |
|--------------|---------------|---------------|---------------|-----------------|----------|---------------|---------------|---------------|-----------------|----------|
|              | **dev (997 sentences)**       |             |               |               |                 | **devtest (1,012 sentences)**    |               |               |               |                 |
| \texttt{hau*}  | 538 (54.0)    | 15,336        | 15,239        | 97             | 24.3     | -             | -             | -             | -               | -        |
| \texttt{nso*}  | 62 (6.2)      | 2,073         | 2,130         | 57             | 29.8     | 53 (5.2)      | 1,780         | 1,819         | 39              | 30.5     |
| \texttt{tso*}  | -             | -             | -             | -              | -        | 61 (6.0)      | 2,127         | 2,161         | 34              | 35.7     |
| \texttt{zul}   | 192 (19.3)    | 3,967         | 3,583         | 384            | 25.7     | 227 (22.4)    | 4,430         | 4,423         | 7               | 30.4     |

**Table:** Data statistics; \# corr. (\%) → number of sentences requiring at least one correction (percentage of original data); \# tokens$_o$ → original token count; \# tokens$_c$ → corrected token count; $\Delta$ tokens → token count difference; \% div. → percentage of token divergence. Languages marked with * indicate corrections are still in progress.

| lang. | dev                                        | devtest                                    |
|-------|--------------------------------------------|--------------------------------------------|
|       | TER Score  | TER # Edits | BLEU   | COMET  | TER Score  | TER # Edits | BLEU   | COMET  |
|-------|------------|-------------|--------|--------|------------|-------------|--------|--------|
| `hau` | 19.6       | 2,702       | 71.4   | 80.4   | -          | -           | -      | -      |
| `nso` | 24.2       | 465         | 66.5   | 73.4   | 24.0       | 392         | 67.7   | 73.5   |
| `tso` | -          | -           | -      | -      | 28.5       | 541         | 64.8   | 72.9   |
| `zul` | 30.0       | 909         | 67.6   | 74.7   | 23.5       | 879         | 70.8   | 75.8   |

**Table:** Similarities between the original and corrected FLORES evaluation data on the four African languages -- original as predictions; corrected as reference translations.

## How to Use

This repository contains the corrected version of the FLORES dataset for the four languages. You can use these corrected datasets for improved performance in evaluating machine translation and other NLP tasks for African languages.

### Accessing the Data
- [Download corrected datasets](link-to-datasets)

## Contributing

We welcome contributions and suggestions to further enhance the dataset. If you would like to contribute, please submit a pull request or open an issue.

## Acknowledgments

Special thanks to the native speaker annotators—university students and researchers—who volunteered to correct translations in their native languages. Their valuable contributions are crucial to the development and preservation of these low-resource languages in NLP.

## Citation

If you use these corrections in your research, please cite our paper:

```
@inproceedings{yourcitation,
  title={Correcting the FLORES Evaluation Dataset for African Languages},
  author={Your name},
  booktitle={Proceedings of the Ninth Conference on Machine Translation (WMT24)},
  year={2024}
}
```

---

We hope these corrections will improve your NLP research and contribute to the growing body of work on African languages!