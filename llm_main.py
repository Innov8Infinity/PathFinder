#Main LLM / StreamLit File 
import streamlit as st
import streamlit.components.v1 as components
from langchain_community.llms import Ollama
import re
import os

# Initialize the Ollama model
llm = Ollama(model="llama3")  # Use the correct model name available in your Ollama setup

# Streamlit layout
st.set_page_config(page_title="Find Your Path", layout="wide")

def fetch_responses():
    try:
        file_path = r'C:\Users\PRINCE\Downloads\project\FlexStart (2)\FlexStart (2)\FlexStart (2)\FlexStart\question_final\data\llm_responses.txt'
        if not os.path.isfile(file_path):
            st.error(f"File not found: {file_path}")
            return ""
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        responses = text.split('\n')
        formatted_response = "<br><br>".join(responses)
        
        topics_regex = r"(\bCGPA\b|\bCourses_Completed\b|\bPreferred_Field\b|\bLearning_Style\b|\bDSA_Marks\b|\bDBMS_Marks\b|\bML_Marks\b|\bMicrocontroller_Marks\b|\bcareer goals\b|\brelevant courses\b)"
        formatted_response = re.sub(topics_regex, r'<span class="highlight">\1</span>', formatted_response, flags=re.IGNORECASE)
        
        link_regex = r"(https?://[^\s]+)"
        formatted_response = re.sub(link_regex, r'<a href="\1" target="_blank">\1</a>', formatted_response)
       
        return formatted_response
    except Exception as e:
        st.error(f"Error fetching the responses: {e}")
        return ""

def fetch_lava_output():
    try:
        file_path = r'C:\Users\PRINCE\Downloads\chatbot\chatbot\lava_model_output.txt'
        if not os.path.isfile(file_path):
            st.error(f"File not found: {file_path}")
            return ""
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        st.error(f"Error fetching the lava model output: {e}")
        return ""

responses_html = fetch_responses()
lava_output = fetch_lava_output()

# Custom CSS for layout and styling
st.markdown("""
    <style>
        .main-content {
            max-width: 800px;
            margin-left: auto;
            margin-right: 5%;
            padding: 1rem;
        }
        .highlight {
            padding: 2px 5px;
            border-radius: 5px;
            font-weight: bold;
        }
        .response a {
            color: #e8491d;
            text-decoration: none;
        }
        .response a:hover {
            text-decoration: underline;
        }
        .stApp {
            margin: 0;
            padding: 0;
        }
    </style>
    """, unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([2, 3])

# Use the first column for the 3D model and lava model output
with col1:
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    st.title("How are you?")

    # Embed the 3D model
    components.html("""
    <div class="sketchfab-embed-wrapper" style="overflow: hidden; height: 400px;"> 
        <iframe title="Teacher Talking" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/4a4ac47a40d84e0aa87707bcd28b081d/embed" style="width: 100%; height: 500px; transform: translateY(-8.5%);"> 
        </iframe> 
        <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> 
            <a href="https://sketchfab.com/3d-models/teacher-talking-4a4ac47a40d84e0aa87707bcd28b081d?utm_medium=embed&utm_campaign=share-popup&utm_content=4a4ac47a40d84e0aa87707bcd28b081d" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> Teacher Talking </a> by 
            <a href="https://sketchfab.com/mizsaidah?utm_medium=embed&utm_campaign=share-popup&utm_content=4a4ac47a40d84e0aa87707bcd28b081d" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> mizsaidah </a> on 
            <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=4a4ac47a40d84e0aa87707bcd28b081d" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
        </p>
    </div>
    """, height=450)


    if lava_output:
        st.markdown(f'<div class="response" style="background: #000000; padding: 20px; margin: 15px 0; border-radius: 10px; font-size: 20px; line-height: 1.8; white-space: pre-wrap;">{lava_output}</div>', unsafe_allow_html=True)
    else:
        st.warning("No lava model output available.")

    st.markdown('</div>', unsafe_allow_html=True)

# Use the second column for the main content
with col2:
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    st.title("PathFinder")

    st.markdown("""
        <div style="background: #50b3a2; color: #ffffff; padding: 30px 0; text-align: center; border-bottom: #e8491d 3px solid; border-radius: 10px 10px 0 0;">
            <h1>Get your own path</h1>
        </div>
        """, unsafe_allow_html=True)

    if responses_html:
        st.markdown(f'<div class="response" style="background: #000000; padding: 20px; margin: 15px 0; border-radius: 10px; font-size: 20px; line-height: 1.8; white-space: pre-wrap;">{responses_html}</div>', unsafe_allow_html=True)
    else:
        st.warning("No responses available.")

    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            try:
                with st.spinner("Generating response..."):
                    response_container = st.empty()
                    full_response = ""
                    for chunk in llm.stream(prompt):
                        full_response += chunk
                        response_container.markdown(full_response)
            except Exception as e:
                st.error(f"Error generating response: {e}")



    st.markdown('</div>', unsafe_allow_html=True)
