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

import GlobalVariable


async def capture():
    cap = cv2.VideoCapture(0)
    while True:
        await asyncio.sleep(1)
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if success:
            GlobalVariable.set_value('is_video_work', True)
        else:
            GlobalVariable.set_value('is_video_work', False)
        # print(img)
        # cv2.imshow("video1", img)
        # cv2.imshow("video2", gray)

    cap.release()
    cv2.destroyAllWindows()
