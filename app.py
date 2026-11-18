import streamlit as st
from groq import Groq
import stream as st
st.set_page_config(page_title = "Placement Practice", page_icon = '🫡', layout= 'centered')
st.title("AI Interview Assistant")
st.caption("Placemrnt practice")
try:
  client = Groq(api_key = st.serets["GROQ_API_KEY"])
except(keyError,FileNotFounf):
  st.error("API key is missing.Add it in advanced settings")
  st.stop()


