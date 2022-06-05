#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：RainDetect.py
#  版本：V2.0
#  author: zhulin
#  说明：雨滴探测传感器实验
#####################################################
import GlobalVariable
import rainDetect.PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import asyncio

makerobo_DO = 18  # 雨滴传感器数字管脚

GPIO.setmode(GPIO.BCM)  # 采用BCM管脚给GPIO口


# GPIO口定义
def makerobo_setup():
    ADC.setup(0x48)  # 设置PCF8591模块地址
    GPIO.setup(makerobo_DO, GPIO.IN)  # 设置雨滴传感器管脚为输入模式


# 打印出雨滴传感器提示信息
def makerobo_Print(x):
    if x == 1:  # 没有雨滴
        GlobalVariable.set_value('is_raining', False)
        # GlobalVariable.set_is_raining(False)
        print('')
        print('   ************************')
        print('   * makerobo Not raining *')
        print('   ************************')
        print('')
    if x == 0:  # 有雨滴
        GlobalVariable.set_value('is_raining', True)
        # GlobalVariable.set_is_raining(True)
        print('')
        print('   **********************')
        print('   * makerobo Raining!! *')
        print('   **********************')
        print('')


# 循环函数
def makerobo_loop():
    makerobo_status = 1  # 雨滴传感器状态
    while True:
        print(ADC.read(0))  # 打印出AIN0的模拟量数值

        makerobo_tmp = GPIO.input(makerobo_DO)  # 读取数字IO口电平，读取数字雨滴传感器DO端口
        if makerobo_tmp != makerobo_status:  # 状态发生改变
            makerobo_Print(makerobo_tmp)  # 打印出雨滴传感器检测信息
            makerobo_status = makerobo_tmp  # 状态值重新赋值
        time.sleep(0.2)  # 延时200ms


async def get_rain_detect():
    makerobo_setup()  # GPIO定义
    makerobo_status = 1  # 雨滴传感器状态
    while True:
        # print('get_rain_detect')
        print(ADC.read(0))  # 打印出AIN0的模拟量数值
        makerobo_tmp = GPIO.input(makerobo_DO)  # 读取数字IO口电平，读取数字雨滴传感器DO端口
        if makerobo_tmp != makerobo_status:  # 状态发生改变
            makerobo_Print(makerobo_tmp)  # 打印出雨滴传感器检测信息
            makerobo_status = makerobo_tmp  # 状态值重新赋值
        await asyncio.sleep(0.2)  # 延时200ms


# 程序入口
if __name__ == '__main__':
    try:
        makerobo_setup()  # GPIO定义
        makerobo_loop()  # 调用循环函数
    except KeyboardInterrupt:
        pass
