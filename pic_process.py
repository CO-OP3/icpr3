#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:47:54 2018

@author: ssy
"""
import cv2  #mac下用：sudo pip install opencv-python==3.3.0.10#
import numpy as np
import matplotlib.pyplot as plt

# 读入图像，并自动转换为numpy的ndarray三维数组
img = cv2.imread('dataset/ICPR_text_train_part1_20180211/image_1000/TB1_2xCLXXXXXcUXFXXunYpLFXX.jpg',cv2.IMREAD_GRAYSCALE)
# 读取图像文件，如果指定了读取的模式，则按照该模式来读取
canny = cv2.Canny(img, 100, 150)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()