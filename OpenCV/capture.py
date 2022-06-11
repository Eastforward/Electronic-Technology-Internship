#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：capture.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/10 15:15 
"""

# import numpy as np
import time
import asyncio
import cv2

# import GlobalVariable
import GlobalVariable


async def capture():
    cap = cv2.VideoCapture(0)
    while True:
        await asyncio.sleep(1)
        success, img = cap.read()
        # print(img)
        face_detect(img)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if success:
            GlobalVariable.set_value('is_video_work', True)
        else:
            GlobalVariable.set_value('is_video_work', False)
        # print(img)
        # cv2.imshow("video1", img)
        # cv2.imshow("video2", gray)

    # cap.release()
    # cv2.destroyAllWindows()


def face_detect(image):
    # image = cv2.imread('./warriors.jpg')
    image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_AREA)
    # 加载分类器模型
    # ---------用下面这种方法找到cascade分类器在哪---------
    # import cv2 as cv
    # print(cv.__file__)

    faceCascade = cv2.CascadeClassifier(
        "/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(2)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5)
    )
    print(3)
    # 逐个标注人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.imshow("dect", image)
    if faces is not None:
        print(faces)
        GlobalVariable.set_value('is_people_detected', True)
    else:
        GlobalVariable.set_value('is_people_detected', False)
    # cv2.waitKey()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    # face_detect()
    capture()
