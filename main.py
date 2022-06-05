#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：main.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/3 15:05 
"""
import time

import humiture.humiture as humiture
import displayer.display as displayer
import rainDetect.RainDetect as RainDetect
import controller.controller as controller
import LED.LED as LED
from threading import Thread
import cv2
import MyThread
import GlobalVariable
import asyncio


async def main():
    task1 = asyncio.create_task(humiture.get_humiture())
    task2 = asyncio.create_task(displayer.show())
    task3 = asyncio.create_task(RainDetect.get_rain_detect())
    task4 = asyncio.create_task(LED.get_LED_detect())
    task5 = asyncio.create_task(controller.detect_input())
    await asyncio.gather(task1, task2, task3, task4, task5)


if __name__ == '__main__':
    GlobalVariable._init()
    humiture.setup()
    displayer.set_text(0, 0, 'Hello world!')
    time.sleep(1)
    # try:
    #     RainDetect.makerobo_setup()  # GPIO定义
    #     RainDetect.makerobo_loop()  # 调用循环函数
    # except KeyboardInterrupt:
    #     pass
    asyncio.run(main())
