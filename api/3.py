import os
import uvicorn
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile
import tensorflow.keras as keras

app = FastAPI()

models_dir = "D:/programing/projects/plant-disease-detection/saved_models"
class_names = ["early blight", "healthy", "late blight"]

# Load "Model 1"
model_path = os.path.join(models_dir, "3")
model = keras.models.load_model(model_path)

def preprocess_image(image):
    # Resize the image to (256, 256)
    image = image.resize((256, 256))
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image[:, :, :3], axis=0)  # Add batch dimension
    return image

@app.post("/predict")
async def predict_image(file: UploadFile):
    # Save the uploaded file
    image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(await file.read())

    # Load and preprocess the image
    image = Image.open(image_path)
    image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(image)
    predicted_class_index = np.argmax(prediction[0])
    predicted_class = class_names[predicted_class_index]

    # Return the predicted class
    return {"prediction": predicted_class}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
