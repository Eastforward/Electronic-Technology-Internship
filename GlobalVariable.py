#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：GlobalVariable.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/3 17:09 
"""


# class GlobalVariable():
#     """
#     全局变量类
#     """
#     humidity = 0
#     temperature = 0
#     is_raining = False
#
#
# def set_humidity(n):
#     GlobalVariable.humidity = n
#
#
# def set_temperature(n):
#     GlobalVariable.temperature = n
#
#
# def get_humidity():
#     return GlobalVariable.humidity
#
#
# def get_temperature():
#     return GlobalVariable.temperature
#
#
# def get_is_raining():
#     return GlobalVariable.is_raining
#
#
# def set_is_raining(flag):
#     GlobalVariable.is_raining = flag


def _init():  # 初始化
    global _global_dict
    _global_dict = {'humidity': 0, 'temperature': 0, 'is_raining': False, 'flag_show_humiture': 1,
                    'flag_show_setting': 0, 'temp_thres': 30, 'addition': ""}


def set_value(key, value):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except:
        print('读取' + key + '失败\r\n')
