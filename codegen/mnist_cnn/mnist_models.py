
import numpy as np
import cv2
import onnxruntime as ort
import os

OUTPUT_PATH="./data"
img_path = "./data/mnist_png/mnist_png/testing/0/10.png"
model_path_q = "./MNISTConvC/quantized/mnist-12-int8.onnx"
model_path = "./MNISTConvC/float/mnist-12.onnx"
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (28,28)).astype(np.float32)/255
input = np.reshape(gray, (1,1,28,28))

ort_sess = ort.InferenceSession(model_path)
outs_hat = ort_sess.run(None, {'Input3': input})[0]

np.save(os.path.join(OUTPUT_PATH, "inp.npy"), input)
np.save(os.path.join(OUTPUT_PATH, "outp.npy"), outs_hat)
