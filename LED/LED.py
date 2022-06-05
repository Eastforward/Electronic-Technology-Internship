#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：LED.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/28 21:03 
"""

import RPi.GPIO as GPIO
import time
import GlobalVariable
import asyncio

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
makerobo_pins = (22, 23)  # PIN管脚字典

# GPIO.setmode(GPIO.BOARD)  # 采用实际的物理管脚给GPIO口
GPIO.setmode(GPIO.BCM)  # 采用BCM管脚给GPIO口
GPIO.setwarnings(False)  # 去除GPIO口警告

GPIO.setup(makerobo_pins, GPIO.OUT)  # 设置Pin模式为输出模式
GPIO.output(makerobo_pins, GPIO.LOW)  # 设置Pin管脚为低电平(0V)关闭LED

p_R = GPIO.PWM(makerobo_pins[0], 2000)  # 设置频率为2KHz
p_G = GPIO.PWM(makerobo_pins[1], 2000)  # 设置频率为2KHz

# 初始化占空比为0(led关闭)
p_R.start(0)
p_G.start(0)


def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def makerobo_set_Color(col):  # 例如:col = 0x1122
    R_val = col >> 8
    G_val = col & 0x00FF
    # 把0-255的范围同比例缩小到0-100之间
    R_val = makerobo_pwm_map(R_val, 0, 255, 0, 100)
    G_val = makerobo_pwm_map(G_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(R_val)  # 改变占空比
    p_G.ChangeDutyCycle(G_val)  # 改变占空比


# 调用循环函数
def makerobo_loop():
    while True:
        for col in colors:
            makerobo_set_Color(col)
            time.sleep(0.5)


# 释放资源
def makerobo_destroy():
    p_G.stop()
    p_R.stop()
    GPIO.output(makerobo_pins, GPIO.LOW)  # 关闭所有LED
    GPIO.cleanup()  # 释放资源


async def get_LED_detect():
    while True:
        # print(GlobalVariable.get_temperature())
        if GlobalVariable.get_value('temperature') >= 29 or GlobalVariable.get_value('is_raining') is True:
            # if GlobalVariable.get_temperature() >= 29 or GlobalVariable.get_is_raining() is True:
            print("Way too hot or raining now!")
            makerobo_set_Color(0x00FF)
            await asyncio.sleep(0.5)  # 延时500ms
            continue
        makerobo_set_Color(0xFF00)
        await asyncio.sleep(0.5)  # 延时500ms


# 程序入口
if __name__ == "__main__":
    try:
        makerobo_loop()  # 调用循环函数
    except KeyboardInterrupt:  # 当按下Ctrl+C时，将执行destroy()子程序。
        makerobo_destroy()  # 释放资源
