import pickle

from fastapi import FastAPI
import torch
import cv2
import numpy as np

torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=False)
app = FastAPI()
model = None


def parse_results(results, model):
    return [{
        'label': model.names[int(res[5])],
        'rect': [float(v) for v in res[:4]],
        'conf': float(res[4]),
    } for res in results.xyxy[0].cpu().detach().numpy()]


@app.get("/")
def read_root():
    return {"version": "1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/yolov5s_detect_image_url")
def yolov5s_detect_image_url(image_url: str):
    global model
    if model is None:
        # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        with open('yolov5s.pkl', 'rb') as f:
            model = pickle.load(f)
    res = model(image_url)
    res = parse_results(res, model)
    print(res)
    return {'results': res}
