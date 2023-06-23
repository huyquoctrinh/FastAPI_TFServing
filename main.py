from typing import Union, Tuple
from typing import Optional, List
from typing import Annotated
from fastapi import FastAPI, UploadFile, File, Form, Request
import cv2 
import numpy as np
import requests
from PIL import Image
import os 
import base64
from io import BytesIO
import io 
from fas_utils import antiSpoofing
from api_model import DetectObject, DetectItem, RequestObject, RequestList

file_name = ""
# model_fas = antiSpoofing(file_name)

def encode(img: str) -> Image.Image:

    img_bytes = base64.b64decode(img.encode('utf-8'))
    return np.asarray(Image.open(io.BytesIO(img_bytes)).convert('RGB'))


def decode(img: Image.Image) -> str:

    try:
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer).decode()
        return img_str
    except:
        return ""


def convert_img(img: str):
    return encode(img)


def get_img_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        img = Image.open(BytesIO(response.content))  
        return img
    except:
        return None


def proccess_detect(req: dict):

    data = req['data']

    all_imgs = []

    for data_dict in data:
        img = data_dict["image"]
        img = encode(img)
        all_imgs.append(img)

    return all_imgs


app = FastAPI()

@app.post("/predict/")

def predict(data: RequestList):
    print("hello")
    req = data.dict()
    # req = data.dict()
    
    # # req = item.dict()
    # # print(req)
    all_imgs = proccess_detect(req)
    # print(len(all_imgs))
    print(len(all_imgs))
    print("img shape:", all_imgs[0].shape)
    # results = model_fas.preidct(all_imgs)
    # score = np.mean(results)

    return {"fas_score": "0"}
