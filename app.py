import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI Interview Assistant", page_icon = '🫡', layout= 'centered')
st.title("AI Interview Asssitant ")
st.caption(" Madhav")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNorFound):
                st.error("API Key is missing . Add it in Advance setting")
                st.stop()
role = st.selectbox("JOB TITLE", ['software engineer','senior software engineer', 'data analyst','prompt engineer', 'Devops engineer', 'other'])
if role == "other":
  st.text_input("Enter your job title ","XXXXXXX")
role = st.selectbox("model", ['openai/gpt-oss-safeguard-20b', 'openai/gpt-oss-120b'])
role = st.selectbox("difficult level", ['bigginer','intermidiate','advance'])
mode = st.radio('Activity', ['generate questions', 'generate code questions', 'evaluate answer','improve answers'])
if mode == 'generate questions':
  count = st.slider(1,10,5)
elif mode == 'generate code questions':
  topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','c++/c','Java','cyber security','ML'])
  count = st.slider("Number od question",1,10,5)
else:
  question = st.text_area('Enter interview question here ')
  answer = st.text_area('enter your answer ', height = 160)
  if st.button("Generate AI Response",type = 'primary'):
    if mode in ['evaluate answer','improve answers'] and (not question.strip())
               st.wrning("plase enter a valid Question and Answer")
               st.stop()
    topics = "topice is" + topic + "difficult is" +level
    if mode ="generate qustions":
      task = 'generate" + str(count) + " frquently asked interview questions, 3 theory and 2 senario questiona.do not give answers.give hints"
    elif mode == "generate code questions":
    task = "generate" + str(count) + " Frequenrtly askedcodeing question on "
  elif mode == "evaluate answer":
    task = "question :" + question + " MY Answer : " + answer + "Evalute this answer based on concept, relevence , communication, length of answe. give each rating out of 5 in a list. "
   elif mode == "improve answers":
     task = "question :" + question + " MY Answer : " + answer + "imporve the answern based oon choice on words key words to include "
        
    
    
