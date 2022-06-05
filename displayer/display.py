#!/usr/bin/env python
import asyncio

import GlobalVariable
import displayer.LCD1602 as LCD1602
import time

flag_show_humiture = 1
flag_show_setting = 0


def setup():
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.write(0, 0, 'Greetings!!')
    LCD1602.write(1, 1, 'WWW.HNZHIYU.CN')
    time.sleep(2)


def set_text(cord1_x, cord1_y, text1, cord2_x=0, cord2_y=1, text2=''):
    LCD1602.init(0x27, 1)  # init(slave address, background light)
    LCD1602.write(cord1_x, cord1_y, text1)
    LCD1602.write(cord2_x, cord2_y, text2)


async def show_humiture():
    now_humi = 0
    now_temp = 0
    global flag_show_humiture, flag_show_setting
    while flag_show_humiture :
        # print('show_humiture')
        try:
            await asyncio.sleep(1)
            humidity, temperature = GlobalVariable.get_humidity(), GlobalVariable.get_temperature()
            if now_humi != humidity or now_temp != temperature:
                now_humi, now_temp = humidity, temperature
                set_text(0, 0, 'Temp={0:0.1f}Cels'.format(temperature), 0, 1,
                         "Humidity={0:0.1f}%".format(humidity))
        except KeyboardInterrupt:
            destroy()


async def show_setting():
    global flag_show_humiture, flag_show_setting
    pass
    # while flag_show_setting:
    #     try:
    #         await asyncio.sleep(1)
    #         set_text(0,0,"Temp thres",0,1,f"") # 重构全局变量

def loop():
    space = '                '
    greetings = 'Thank you for buying ZHIYU Sensor Kit for Raspberry! ^_^'
    greetings = space + greetings
    while True:
        tmp = greetings
        for i in range(0, len(greetings)):
            LCD1602.write(0, 0, tmp)
            tmp = tmp[1:]
            time.sleep(0.8)
            LCD1602.clear()


def destroy():
    pass


if __name__ == "__main__":
    try:
        setup()
        while True:
            pass
    except KeyboardInterrupt:
        destroy()
