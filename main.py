import streamlit as st
from utils import pipe, generate_highlighted_words


# for custom CSS styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title('تطبيق تصنيف الكلمات')

with st.form('submission_form'):
    text = st.text_area('من فضلك ادخل النص:', placeholder='ادخل النص المراد تصنيفه...', height=80)
    submitted = st.form_submit_button('تأكيد')

    if submitted:
        if text:
            with st.spinner('جاري التحميل'):
                model_output = pipe(text, grouped_entities=True)

            words = [item['word'] for item in model_output]
            entities = [item['entity_group'] for item in model_output]

            rendered_text = generate_highlighted_words(words, entities)
            
            st.write('<p class="bold-text"> النتيجة المتوقعة: </p>', unsafe_allow_html=True)
            st.write(rendered_text, unsafe_allow_html=True)

        else:
            st.error('من فضلك ادخل النص المراد تصنيفه')
