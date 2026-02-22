
import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Charge les variables du fichier .env dans l'environnement système
load_dotenv()

app = FastAPI()

# Récupération avec os.getenv (plus propre) et typage
API_CST = os.getenv("API_CST")
# On définit une valeur par défaut (ex: 8000) pour éviter que le int() ne plante si la variable est absente
API_PORT = int(os.getenv("API_PORT", 8000))

@app.get("/")
def read_root():
    return {"API_CST": API_CST, "API_PORT": API_PORT}
