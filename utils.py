from transformers import pipeline


pipe = pipeline('token-classification', 'mohammedaly2222002/xlm-roberta-base-finetuned-ud-arabic')

class_mapper = {
    'VERB': 'فعل',
    'NOUN': 'اسم',
    'ADJ': 'صفة',
    'ADP': 'حرف جر',
    'PUNCT': 'علامة ترقيم',
    'NUM': 'رقم',
    'X': 'غير مصنف',
    '_': '_',
    'PRON': 'ضمير',
    'SCONJ': 'اقتران تابع',
    'CCONJ': 'حرف عطف',
    'DET': 'محدد',
    'PART': 'جزء',
    'ADV': 'ظرف',
    'SYM': 'رمز',
    'AUX': 'فعل مساعد',
    'PROPN': 'اسم مناسب',
    'INTJ': 'INTJ'
}



def generate_highlighted_words(words, entities):
    rendered_text = '<div class="highlighted-text"> '
    
    for word, entity in zip(words, entities):
        highlight_word = f' <span class="highlight-{entity}"> ' + word + f' <span class="highlight-inner-{entity}"> ' + class_mapper[entity] + " </span> " + " </span> "
        rendered_text += highlight_word

    rendered_text += ' </div>'

    return rendered_text