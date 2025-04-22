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

## 📁 Estructura del Proyecto

```bash
ApiDermatoss/
│
├── main.py              # Código principal FastAPI
├── Dockerfile           # Imagen Docker
├── requirements.txt     # Dependencias
├── vgg11_NewF-model.pt  # Modelo
├── .gitignore

