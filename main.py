from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from torchvision import models, transforms
import torch
from torch import nn
from PIL import Image
import io

# Inicializar la app
app = FastAPI()

# Definir las clases
class_names = ["ampolla", "mancha", "pustula", "roncha"]  # <- Ajusta si tu orden es diferente

# Preprocesamiento igual al usado durante el entrenamiento
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Tamaño estándar para VGG
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImagenNet stats
                         std=[0.229, 0.224, 0.225])
])

# Cargar el modelo (igual estructura que el de entrenamiento)
model = models.vgg11_bn(pretrained=False)
model.classifier[6] = nn.Linear(in_features=4096, out_features=4)  # 4 clases

# Cargar pesos entrenados
model.load_state_dict(torch.load("vgg11_NewF-model.pt", map_location=torch.device("cpu")))
model.eval()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Leer imagen
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Preprocesar imagen
        input_tensor = transform(image).unsqueeze(0)  # [1, 3, 224, 224]

        # Predicción
        with torch.no_grad():
            outputs = model(input_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)
            predicted_class = torch.argmax(probs, dim=1).item()

        return JSONResponse(content={
            "predicted_class": predicted_class,
            "predicted_label": class_names[predicted_class],
            "probabilities": probs.squeeze().tolist()
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
