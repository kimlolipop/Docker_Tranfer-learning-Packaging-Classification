from fastapi import FastAPI
from tensorflow.keras.models import load_model
from urllib.request import urlopen
from data import Prediction
import uvicorn
import tensorflow as tf
import numpy as np
import cv2
import json


app = FastAPI()

def load_map_class():
  with open('map_cls.json','r') as fp:
    label_map = json.load(fp)
  
  return label_map

def url_to_imgae(url, readFlag=cv2.IMREAD_COLOR):
  resp = urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype="uint8")
  image = cv2.imdecode(image, readFlag)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  return image

@app.post('/getclass')
async def predict_class(body:Prediction):
  dim = (224,224)
  label_map = load_map_class()
  model_s4 = load_model('model/weights_best_s4_50.h5')
  image = url_to_imgae(body.image_link)
  image = cv2.resize(image,dim)
  image = image.reshape(1,224,224,3)
  image = image / 255.
  ans = model_s4.predict(image)
  ans = list(map(np.vectorize(label_map.get), str(np.argmax(ans, axis=-1)[0])))
  ans = ans[0].tolist()

  return ans


if __name__ == '__main__':
  uvicorn.run('app:app',port=7001,reload=True)
