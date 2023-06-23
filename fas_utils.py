import cv2
import joblib
import numpy as np
import os
import tensorflow as tf

class antiSpoofing:
    def __init__(self, model_file):
        if not os.path.exists(model_file):
            raise ValueError(
                "model anti-spoofing {} is not exist".format(model_file))
        self.model = joblib.load(model_file)

    def _calc_hist(self, img):
        histogram = [0] * 3
        for j in range(3):
            histr = cv2.calcHist([img], [j], None, [256], [0, 256])
            histr *= 255.0 / histr.max()
            histogram[j] = histr
        return np.array(histogram)

    def predict(self, face_arr):
        if face_arr is None or len(face_arr) == 0:
            return -1
        else:
            return self.model.predict_proba(face_arr)
