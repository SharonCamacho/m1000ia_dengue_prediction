import uvicorn
from fastapi import FastAPI, HTTPException
import joblib
from dengue import MonthData
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

model = load_model("dengue_lstm_model.h5")

@app.get('/')
def index():
    return FileResponse('static/index.html')

@app.post('/dengue/predict')
async def predict_dengue_type(data: MonthData):
    try:
        data_array = np.array([
            data.month1, data.month2, data.month3, data.month4,
            data.month5, data.month6, data.month7, data.month8,
            data.month9, data.month10, data.month11, data.month12
        ])
        data_array = data_array.reshape(1, 12)
        prediction = model.predict(data_array)
        
        print("Type of prediction:", type(prediction))
        print("Shape of prediction:", prediction.shape)
        print("Cantidad de Casos el próximo mes:", prediction)
        
        # Try to convert the prediction to a simple Python type
        if prediction.shape == (1, 1):
            prediction_value = int(prediction[0][0])
            print(prediction_value)
        else:
            prediction_value = prediction.flatten().tolist()
            print(prediction_value)
        return {
            'prediction': prediction_value
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)