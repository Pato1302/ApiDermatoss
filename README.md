# 🧠 Dermatoss API - Clasificación de Imágenes Dermatológicas

API para clasificación automática de imágenes dermatológicas usando una CNN basada en VGG11 entrenada con PyTorch.

---

## 🚀 Requisitos

- Docker instalado
- Git instalado
- Puerto 8000 abierto en el grupo de seguridad (si usas EC2)
- Archivo `.pt` del modelo (descargable o copiado manualmente)
- FastAPI y Python 3.9+ en el contenedor

---

## 📦 Clonar el Repositorio

```bash
git clone https://github.com/Pato1302/ApiDermatoss.git
cd ApiDermatoss
```

## 🐳 Construir la Imagen Docker
```bash
sudo docker build -t dermatoss-api .
```
Esto construirá la imagen Docker con las dependencias desde requirements.txt.

## ▶️ Ejecutar el Contenedor
```bash
Copiar
Editar
sudo docker run -d -p 8000:8000 dermatoss-api
-d: modo en segundo plano

-p 8000:8000: expone el puerto 8000
```
## 🌐 Acceder a la API
En el navegador o Postman:

```arduino
http://<IP-DEL-SERVIDOR>:8000/predict
```

## 🧪 Endpoint
### POST /predict
Descripción: Sube una imagen y obtiene la clase dermatológica.

Ejemplo con curl:

```bash
curl -X 'POST' \
  'http://<IP-DEL-SERVIDOR>:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@tu_imagen.jpg'
```

## 💻 Conexión desde Wix
Desde el backend de Wix puedes hacer una llamada HTTP como esta:

```js
import { fetch } from 'wix-fetch';

fetch("http://<IP-DEL-SERVIDOR>:8000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "multipart/form-data"
  },
  body: archivoDeImagen // Usa FormData
})
.then(response => response.json())
.then(data => console.log("Resultado:", data));
```
Asegúrate que tu servidor tenga una IP pública accesible y que el CORS esté configurado correctamente en FastAPI si vas a llamar desde el frontend.


## ☁️ Uso en AWS EC2
Sube el archivo .pt manualmente si es grande (vía scp):

```bash
scp -i ia_api-key.pem vgg11_NewF-model.pt ec2-user@<IP>:~/ApiDermatoss/
```
Asegúrate de tener permisos adecuados:

```bash
chmod 400 ia_api-key.pem
```
Conéctate a tu instancia:

```bash
ssh -i ia_api-key.pem ec2-user@<IP>
```
Luego repite los pasos de git clone, docker build y docker run.

## 📁 Estructura del Proyecto

```bash
ApiDermatoss/
│
├── main.py              # Código principal FastAPI
├── Dockerfile           # Imagen Docker
├── requirements.txt     # Dependencias
├── vgg11_NewF-model.pt  # Modelo
├── .gitignore
```
