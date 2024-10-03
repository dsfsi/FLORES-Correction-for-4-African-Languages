# FLORES Dataset Corrections for Four African Languages

This project focuses on correcting the FLORES evaluation dataset (dev and devtest) for four African languages: **Hausa**, **Northern Sotho (Sepedi)**, **Xitsonga**, and **isiZulu**. The original dataset, though groundbreaking in covering low-resource languages, contained several inconsistencies and inaccuracies in these languages, which could affect the quality of evaluations in Natural Language Processing (NLP) tasks, especially for machine translation.

## Overview

In this project, native speakers meticulously reviewed and corrected the dataset to ensure improved accuracy and reliability for each language. Our goal was to enhance the integrity of downstream NLP tasks that use this data.

### What We Did:
1. **Reviewed and Corrected Errors**: Identified and implemented corrections to translation inconsistencies and inaccuracies in the dataset.
2. **Statistical Analysis**: Conducted statistical comparisons between the original and corrected datasets, highlighting the differences and improvements made.
3. **Improved Dataset Quality**: Enhanced linguistic accuracy and reliability, ensuring more effective evaluation of NLP tasks involving these languages.

### Key Corrections:
- **Hausa**: The Hausa translations revealed numerous inconsistencies, suggesting a significant portion may have been automatically generated, particularly due to unclear or incoherent phrasing. Comparisons with the Hausa FLORES dataset and Google Translate showed that many lexical choices were incorrect and aligned with Google’s outputs, raising concerns about the quality of the original translations. Additional issues included improper translations of named entities and the frequent omission of special characters in standardized Hausa alphabets.
- **Northern Sotho (Sepedi)**: The translations in Northern Sotho displayed a need for improvement in vocabulary consistency, syntax, and the accurate conveyance of technical terms. While most text was accurately translated, minor corrections were necessary to enhance clarity, including adjustments for borrowed words and proper spacing. Notably, some translations omitted important terms, affecting the overall meaning, such as leaving out “scientific” when referring to tools.
- **Xitsonga**: In Xitsonga translations, several vocabulary accuracy issues and improper use of borrowed terms were identified, leading to misunderstandings. Errors included incorrect translations for phrases like "Type 1 diabetes" and uniform translations lacking contextual variation, which hindered clarity. Spelling errors and the inappropriate borrowing of terms significantly impacted translation quality, underscoring the need for proper native language usage.
- **isiZulu**: IsiZulu translations faced challenges with vocabulary inconsistencies, syntax errors, and issues in expressing technical terms, compounded by the language's agglutinative structure. Key problems included incorrect grammatical structures for time expressions and the unnecessary borrowing of English terms, which disrupted linguistic flow. Efforts to standardize terminology throughout the translations were made to ensure grammatical accuracy and clarity.

### Evaluating the Corrections:

<table>
  <tr>
    <td rowspan="2">
      lang.
    </td>
    <td colspan="5">
      dev (997 sentences)
    </td>
    <td>
    </td>
    <td colspan="5">
      devtest (1,012 sentences)
    </td>
  </tr>
  <tr>
    <td>#corr. (%)</td>
    <td>#tokens<sub>o</sub></td>
    <td>#tokens<sub>c</sub></td>
    <td>&Delta; tokens</td>
    <td>% div.</td>
    <td>
    </td>
    <td>#corr. (%)</td>
    <td>#tokens<sub>o</sub></td>
    <td>#tokens<sub>c</sub></td>
    <td>&Delta; tokens</td>
    <td>% div.</td>
  </tr>
  <tr>
    <td>hau</td>
    <td>538 (54.0)</td>
    <td>15,336</td>
    <td>15,239</td>
    <td>97</td>
    <td>24.3</td>
    <td></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>nso</td>
    <td>62 (6.2)</td>
    <td>2,073</td>
    <td>2,130</td>
    <td>57</td>
    <td>29.8</td>
    <td></td>
    <td>53 (5.2)</td>
    <td>1,780</td>
    <td>1,819</td>
    <td>39</td>
    <td>30.5</td>
  </tr>
  <tr>
    <td>tso</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td></td>
    <td>61 (6.0)</td>
    <td>2,127</td>
    <td>2,161</td>
    <td>34</td>
    <td>35.7</td>
  </tr>
  <tr>
    <td>zul</td>
    <td>192 (19.3)</td>
    <td>3,967</td>
    <td>3,583</td>
    <td>384</td>
    <td>25.7</td>
    <td></td>
    <td>227 (22.4)</td>
    <td>4,430</td>
    <td>4,423</td>
    <td>7</td>
    <td>30.4</td>
  </tr>
</table>

**Table:** Data statistics; #corr. (%) → number of sentences requiring at least one correction (percentage of original data); #tokens<sub>o</sub> → original token count; #tokens<sub>c</sub> → corrected token count; &Delta; tokens → token count difference; % div. → percentage of token divergence. Languages marked with * indicate corrections are still in progress.

<table>
  <tr>
    <td rowspan="3">
      lang.
    </td>
    <td colspan="4">
      dev
    </td>
    <td>
    </td>
    <td colspan="4">
      devtest
    </td>
  </tr>
  <tr>
    <td colspan="2">TER</td>
    <td rowspan="2">BLEU</td>
    <td rowspan="2">COMET</td>
    <td></td>
    <td colspan="2">TER</td>
    <td rowspan="2">BLEU</td>
    <td rowspan="2">COMET</td>
  </tr>
  <tr>
    <td>Score</td>
    <td>#Edits</td>
    <td></td>
    <td>Score</td>
    <td>#Edits</td>
  </tr>
  <tr>
    <td>hau</td>
    <td>19.6</td>
    <td>2,702</td>
    <td>71.4</td>
    <td>80.4</td>
    <td></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>nso</td>
    <td>24.2</td>
    <td>465</td>
    <td>66.5</td>
    <td>73.4</td>
    <td></td>
    <td>24.0</td>
    <td>392</td>
    <td>67.7</td>
    <td>73.5</td>
  </tr>
  <tr>
    <td>tso</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td></td>
    <td>28.5</td>
    <td>541</td>
    <td>64.8</td>
    <td>72.9</td>
  </tr>
  <tr>
    <td>zul</td>
    <td>30.0</td>
    <td>909</td>
    <td>67.6</td>
    <td>74.7</td>
    <td></td>
    <td>23.5</td>
    <td>879</td>
    <td>70.8</td>
    <td>75.8</td>
  </tr>
</table>

**Table:** Similarities between the original and corrected FLORES evaluation data on the four African languages - original as predictions; corrected as reference translations.

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
@misc{abdulmumin2024correctingfloresevaluationdataset,
  title={Correcting FLORES Evaluation Dataset for Four African Languages}, 
  author={Idris Abdulmumin and Sthembiso Mkhwanazi and Mahlatse S. Mbooi and Shamsuddeen Hassan Muhammad and Ibrahim Said Ahmad and Neo Putini and Miehleketo Mathebula and Matimba Shingange and Tajuddeen Gwadabe and Vukosi Marivate},
  year={2024},
  eprint={2409.00626},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2409.00626}, 
}
```

---

We hope these corrections will improve your NLP research and contribute to the growing body of work on African languages!