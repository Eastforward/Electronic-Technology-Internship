#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：test.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/10 15:15 
"""

# import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("video1", img)
    cv2.imshow("video2", gray)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
