import requests
import streamlit as st

API_URL_Semantics = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
API_URL_Captions = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def generate_semantics(file):
    response = requests.post(API_URL_Semantics, headers=headers, data=file)
    return response.json()

def generate_captions(payload):
    response = requests.post(API_URL_Captions, headers=headers, json=payload)
    return response.json()[0]['generated_text']

st.title("Caption Generator")

file = st.file_uploader("Upload an image", type=['jpg','jpeg','png'])

if file:
    col1, col2 = st.columns(2)
    with col1:
        st.image(file, use_column_width=True)

    with col2:
        with st.spinner("Generating Semantics....."):
            semantics = generate_semantics(file)

        with st.spinner("Generating Captions...."):
            prompt_dic = {
                "inputs": f"Question: Convert the following image semantics {semantics} into an Instagram caption with relevant hashtags and emojis. Answer:"
            }
            caption_raw = generate_captions(prompt_dic)
            st.subheader("Caption")

            # Process the response to remove unnecessary text
            if "Answer:" in caption_raw:
                caption = caption_raw.split("Answer: ")[1].strip()
            else:
                caption = caption_raw.strip()

            st.write(caption)
