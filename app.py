from fastapi import FastAPI, File, Form, UploadFile
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from io import StringIO

app = FastAPI()
model_predict = pickle.load(open("model.pkl", "rb"))

class Model(BaseModel):
    Nombre_Apellido: str
    
@app.get('/')
def index():
    return {'message': 'La API ANDA =) '}
    

# Request body
@app.post("/api/")
def model(api: Model):
    # Import the saved model
    CATEGORIA = model_predict.classify({'last_letter': api.Nombre_Apellido})

    return {"Pertenece a la categoría de": CATEGORIA}
    
   
            


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)
    
   
            
 