from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = FastAPI()

model = tf.keras.models.load_model("dog_cat_classification.h5")
class_names = ["Dog", "Cat"]

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File()):
    image_bytes = await file.read()
    input_tensor = preprocess_image(image_bytes)
    prediction = model.predict(input_tensor)
    predicted_class = int(prediction[0][0] > 0.5)
    score = float(prediction[0][0])
    confidence = score if predicted_class == 1 else 1 - score
    label = class_names[predicted_class]
    return JSONResponse({"class": label, "confidence": round(confidence, 2)})
