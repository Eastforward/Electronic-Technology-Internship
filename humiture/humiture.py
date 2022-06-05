#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FirstWork 
@File ：humiture.py
@IDE  ：PyCharm 
@Author ：Eastforward
@Date ：2022/5/3 15:16 
"""

import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import asyncio
import GlobalVariable

Sensor = 11
humiture = 17


def setup():
    print('Setting up, please wait...')


def loop():
    while True:
        humidity, temperature = DHT.read_retry(Sensor, humiture)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}°  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')


async def get_humiture():
    while True:
        # print('get_humiture')
        await asyncio.sleep(0.1)
        humidity, temperature = DHT.read_retry(Sensor, humiture)
        GlobalVariable.set_humidity(humidity)
        GlobalVariable.set_temperature(temperature)
        print(GlobalVariable.get_humidity(), GlobalVariable.get_temperature())


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
