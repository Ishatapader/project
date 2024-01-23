import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = 'gemini-pro'

st.title("Speech Generator")
aoi=["10th","12th","Bachalors","Masters","PHD","Diploma"]

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input('Name')
    age = st.text_input('Age')
    education= st.multiselect('Education',options=aoi)
with col2:
    state = st.text_input('State ')
    designation = st.text_input('Designation ')
    gender = st.selectbox('Gender',options=['Male','Female'])
    
with col3:
    institute = st.text_input('Institute')
    topic = st.text_input('Topic')
    language = st.selectbox('Language of Introduction',['English','Hindi','Bengali','French','Spanish','Nepali'])
contents = 'A person whose name is '+name+'. topic is '+topic+'. Age is '+age+'. Level of education is '+",".join(education)
contents += '. Lives in state of '+state+' The designation of the person is '+designation+'.'
contents += 'Gender is '+gender+'. And Institute name is '+institute+'.'
contents += 'Write a proper speech for me which i will  give to others and it will be profesional which will be within 50 to 100 words with some bullet points and provide the speech regaurding the designation and the topic. Language of the introduction would be'+language+'.'
a = st.button('Generate')
if a:
    with st.spinner('Wait for it'):
        gemini = genai.GenerativeModel(model_name=model)
        response = gemini.generate_content(contents,stream=False)
        st.text_area(label ="",value=response.text,height=500)
    st.success('Done')
