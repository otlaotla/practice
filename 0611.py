import streamlit as st
import os
from langchain_community.chat_models import ChatOpenAI

# 페이지 설정
st.set_page_config(page_title="Pregunta lo que quieras")
st.title("Pregunta lo que quieras, estoy aquí para ayudarte")

# OpenAI API 키 설정 (secrets에서 가져오기)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 응답 생성 함수
def generate_response(input_text):
    llm = ChatOpenAI(temperature=0, model_name='gpt-4')
    response = llm.predict(input_text)
    return response

# 폼 생성 (메인 스트림릿 코드에서 폼 실행)
with st.form('Question'):
    text = st.text_area('Escribe tu pregunta:', 
                         "Qué tipo de modelos de texto proporciona OpenAI?")
    submitted = st.form_submit_button('ENVIAR')

# 제출 버튼을 눌렀을 때
if submitted:
    response =
