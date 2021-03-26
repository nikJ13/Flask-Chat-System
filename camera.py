# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:59:18 2021

@author: anujjain
"""
import cv2


def takephoto():
    cam = cv2.VideoCapture(0)
    for i in range(1):
        return_val, img = cam.read()
#print(img)
    return img