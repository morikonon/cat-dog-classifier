import streamlit as st
import requests
from PIL import Image

st.title("Cat or Dog Classification")

uploaded_file = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Classify"):
        with st.spinner("Sending to the server..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://127.0.0.1:8000/predict", files=files)

            if response.status_code == 200:
                result = response.json()
                st.success(f"Result: **{result['class']}** (confidence: {result['confidence'] * 100:.1f}%)")
            else:
                st.error("Error from server")
