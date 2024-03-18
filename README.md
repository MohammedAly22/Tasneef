# "Tasneef - تصنيف" | An Arabic POS Tagger
[![Running Demo](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg)](https://tasneef.streamlit.app/]
In natural language processing (NLP), **Part of Speech (POS)** refers to the **grammatical category** or syntactic function that a word serves in a sentence. It's a way of **categorizing words** based on their roles within the structure of a sentence. POS tagging involves assigning a specific label, such as `noun`, `verb`, `adjective`, `adverb`, etc., to each word in a sentence.

Here are some common parts of speech:
| Tag              | Arabic Tag | Description |
| :---------------- | ------: | :---- |
| Noun (N)        |   اسم   | Represents a person, place, thing, or idea. Examples: dog, city, happiness. |
| Verb (V)           |   فعل   | Describes an action or occurrence. Examples: run, eat, sleep. |
| Adjective (ADJ)    |  صفة   | Modifies or describes a noun. Examples: happy, tall, red. |
| Adverb (ADV) |  حال   | Modifies or describes a verb, adjective, or other adverb. Examples: quickly, very, well. |
| Pronoun (PRON) |  ضمير   | Replaces a noun. Examples: he, she, it. |
| Preposition (PREP) |  حرف جر   | Indicates relationships between words, often in terms of time or place. Examples: in, on, under. |
| Conjunction (CONJ) |  اقتران   | Connects words, phrases, or clauses. Examples: and, but, or. |
| Interjection (INTJ) |  تعجب   | Expresses strong emotion. Examples: wow, oh, ouch. |

**POS tagging** is an essential task in NLP because understanding the grammatical structure of a sentence helps machines **comprehend the meaning and context of the text**. It's particularly useful in applications like **text analysis**, **information retrieval**, and **language translation**.

# Demo:
https://github.com/MohammedAly22/Tasneef/assets/90681796/299ede6e-326d-4aef-8bbf-84d78e1b7596


# Usage:
## Downloading and Running Tasneef Locally:
1. Clone this repository
```git
git clone https://github.com/MohammedAly22/Tasneef
```

2. Inside the project folder, run the demo using the following command
```
streamlit run main.py
```

## Use the Model as a Hugging Face pipeline:
```python
from transformers import pipeline

pos_tagger = pipeline("token-classification", "mohammedaly2222002/xlm-roberta-base-finetuned-ud-arabic")
text = "اشترى خالد سيارة، و أصبح يمتلك 3 سيارات."

predictions = pos_tagger(text)
words = [item["word"] for item in predictions]
predicted_entities = [item["entity"] for item in predictions]


print(f"words:    {words}")
print(f"entites:  {predicted_entities}")
```

**output**:
```
words:    ['▁اشتر', 'ى', '▁خالد', '▁سيارة', '،', '▁و', '▁أصبح', '▁يمتلك', '▁3', '▁سيارات', '.']
entites:  ['VERB', 'VERB', 'X', 'NOUN', 'PUNCT', 'CCONJ', 'VERB', 'VERB', 'NUM', 'NOUN', 'PUNCT']
```

# Dataset
The [Arabic-PADT UD treebank](https://github.com/UniversalDependencies/UD_Arabic-PADT) is based on the Prague Arabic Dependency Treebank (PADT), created at the Charles University in Prague.

The treebank consists of **7,664** sentences (282,384 tokens) and its domain is mainly **newswire**. The annotation is licensed under the terms of CC BY-NC-SA 3.0 and its original (non-UD) version can be downloaded from http://hdl.handle.net/11858/00-097C-0000-0001-4872-3.

The morphological and syntactic annotation of the Arabic UD treebank is created through the conversion of PADT data. The conversion procedure has been designed by Dan Zeman. The main coordinator of the original PADT project was Otakar Smrž.

Here is the first sample from the `ar_padt-ud-test.conllu` file:
```
# newdoc id = assabah.20041005.0017<br>
# newpar id = assabah.20041005.0017:p1<br>
# sent_id = assabah.20041005.0017:p1u1<br>
# text = <br>سوريا: تعديل وزاري واسع يشمل 8 حقائب
# orig_file_sentence ASB_ARB_20041005.0017#1<br>
1	سوريا	سُورِيَا	X	X---------	Foreign=Yes	0	root	0:root	SpaceAfter=No|Vform=سُورِيَا|Gloss=Syria|Root=sUr|Translit=sūriyā|LTranslit=sūriyā<br>
2	:	:	PUNCT	G---------	_	1	punct	1:punct	Vform=:|Translit=:<br>
3	تعديل	تَعدِيل	NOUN	N------S1I	Case=Nom|Definite=Ind|Number=Sing	6	nsubj	6:nsubj<br>	Vform=تَعدِيلٌ|Gloss=adjustment,change,modification,amendment|Root=_d_l|Translit=taʿdīlun|LTranslit=tadīl<br>
4	وزاري	وِزَارِيّ	ADJ	A-----MS1I	Case=Nom|Definite=Ind|Gender=Masc|Number=Sing	3	amod	3:amod<br>	Vform=وِزَارِيٌّ|Gloss=ministry,ministerial|Root=w_z_r|Translit=wizārīyun|LTranslit=wizārīy<br>
5	واسع	وَاسِع	ADJ	A-----MS1I	Case=Nom|Definite=Ind|Gender=Masc|Number=Sing	3	amod	3:amod<br>	Vform=وَاسِعٌ|Gloss=wide,extensive,broad|Root=w_s_|Translit=wāsiʿun|LTranslit=wāsi<br>
6	يشمل	شَمِل	VERB	VIIA-3MS--	Aspect=Imp|Gender=Masc|Mood=Ind|Number=Sing|Person=3|VerbForm=Fin|Voice=Act	1	parataxis	1:parataxis<br>	Vform=يَشمَلُ|Gloss=comprise,include,contain|Root=^s_m_l|Translit=yašmalu|LTranslit=šamil<br>
7	8	8	NUM	Q---------	NumForm=Digit	6	obj	6:obj	Vform=٨|Translit=8<br>
8	حقائب	حَقِيبَة	NOUN	N------P2I	Case=Gen|Definite=Ind|Number=Plur	7	nmod	7:nmod:gen<br>	Vform=حَقَائِبَ|Gloss=briefcase,suitcase,portfolio,luggage|Root=.h_q_b|Translit=ḥaqāʾiba|LTranslit=ḥaqībat<br>
```

# Results
Here is the table of results after fine-tuning for 3 epochs:
| Epoch              | Training Loss | Validation Loss | F1 | Accuracy |
| ---------------- | ------ | ---- |  ---- |  ---- |
| 1 | 0.188700 | 0.113953 | 0.958816 | 0.971454 |
| 2 | 0.090000 | 0.090725 | 0.966489 | 0.976796 |
| 3 | 0.055800 | 0.091719 | 0.969978 | 0.979393 |

classification report:
![download](https://github.com/MohammedAly22/Tasneef/assets/90681796/eb9857e7-5bc0-460f-b3d6-ef31c94c68b1)
