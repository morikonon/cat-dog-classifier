# 🐱🐶 Cat vs Dog Classifier

This is a simple image classification project that uses a pre-trained TensorFlow model to classify uploaded images as either a **cat** or a **dog**.

The project is built using:

- ⚡️ **FastAPI** — backend API for model inference  
- 🌐 **Streamlit** — frontend for user interaction  
- 🧠 **TensorFlow** — for deep learning model  
- 📡 **HTTP requests** — to connect frontend and backend  

---

## 🚀 Features

- Upload image via web UI  
- Automatically send image to backend for classification  
- View predicted label (cat or dog) with confidence score  
- Works with `.jpg`, `.jpeg`, `.png` files  

---

## 📁 Project Structure

cat_dog_classifier/
|
├── main.py # FastAPI backend
├── dog_cat_classification.h5 # Trained TensorFlow model

├── app.py # Streamlit frontend
├── requirements.txt # List of dependencies
└── README.md # Project description


---

## 🧠 Model

The model is a binary classifier built with TensorFlow/Keras and trained to distinguish cats and dogs.  
It expects an input image resized to **224x224**, normalized to `[0, 1]`, and outputs a single probability (`> 0.5` = dog, `< 0.5` = cat).

## Model Download

The trained model file `dog_cat_classification.h5` is not included in this repository due to its large size.

You can download the model using this link:  
[Download model from Google Drive](https://drive.google.com/file/d/15VVHXPvQDnIzV-D_t1AWcbvgagIpocXn/view?usp=share_link)

After downloading, place the model file in the root directory of the project or update the model path in the code accordingly.
---

## Jupyter Notebook

The cat_dog_classification.ipynb notebook contains the complete code for training the cat vs dog classification model, including data preprocessing, model architecture, training process, and saving the trained model.

If you want to retrain the model or experiment with the training process, open this notebook in Jupyter or Google Colab and run the cells step-by-step.

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cat-dog-classifier.git
cd cat-dog-classifier

2. Install dependencies
pip install -r requirements.txt

3. Run the FastAPI backend
uvicorn app.main:app --reload

4. Run the Streamlit app
streamlit run streamlit_app.py

Requirements:
All dependencies are listed in requirements.txt. Main libraries include:

fastapi
uvicorn
streamlit
requests
tensorflow
pillow
numpy

Notes

Make sure dog_cat_classification.h5 is in the correct path ().
You can train your own model or use the provided one.
You can deploy this project on platforms like Render, Hugging Face Spaces, or Heroku.

Example Prediction

Input: uploaded image
Output: "class": "cat", "confidence": 0.92

Contact

Made by [Mukhamedali Daniyaruly].
Feel free to contact me for feedback, questions or suggestions!

