import torch
import pickle


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
with open('yolov5s.pkl', 'wb') as f:
    pickle.dump(model, f)
