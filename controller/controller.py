import time

import RPi.GPIO as GPIO
import asyncio

import GlobalVariable

setting_button = 18  # 选定温度阈值的开关,BCM编码
down_button = 27
up_button = 24

buttons = [0, 0, 0]


# 初始化GPIO口
def makerobo_setup():
    GPIO.setmode(GPIO.BCM)  # 采用实际的物理管脚给GPIO口
    GPIO.setwarnings(False)  # 去除GPIO口警告
    # GPIO.setup(makerobo_Rpin, GPIO.OUT)  # 设置红色LED管脚为输出模式
    # GPIO.setup(makerobo_Gpin, GPIO.OUT)  # 设置绿色LED管脚为输出模式
    # GPIO.setup(makerobo_BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置BtnPin管脚为输入模式，上拉至高电平(3.3V)
    # # 中断函数，当轻触按键按下时，调用detect函数
    # GPIO.add_event_detect(makerobo_BtnPin, GPIO.BOTH, callback=makerobo_detect, bouncetime=200)


# 双色LED模块驱动子函数
def double_colorLED(x, btn):
    if x == 0:  # x为0时，开启红色LED灯
        pass
        # print(x)
        # GPIO.output(makerobo_Rpin, 1)
        # GPIO.output(makerobo_Gpin, 0)
    if x == 1:  # x为1时，开启绿色LED灯
        pass
        # print(x)
        # GPIO.output(makerobo_Rpin, 0)
        # GPIO.output(makerobo_Gpin, 1)


# 打印函数，显示出按键按下
def makerobo_Print(x, btn):
    if x == 0:
        print('***************************************')
        print(f'* {btn} Button Pressed!   *')
        print('***************************************')


# 中断函数，有按键按下时，响应中断函数
def setting_button_detect(btn):
    double_colorLED(GPIO.input(btn), btn)  # 调用双色LED驱动函数
    makerobo_Print(GPIO.input(btn), btn)  # 打印出GPIO的状态


def down_button_detect(btn):
    double_colorLED(GPIO.input(btn), btn)  # 调用双色LED驱动函数
    makerobo_Print(GPIO.input(btn), btn)  # 打印出GPIO的状态


# 循环函数
def makerobo_loop():
    while True:
        pass


# 释放资源
def makerobo_destroy():
    # GPIO.output(makerobo_Gpin, GPIO.LOW)  # 关闭绿色LED
    # GPIO.output(makerobo_Rpin, GPIO.LOW)  # 关闭红色LED
    GPIO.cleanup()  # 释放资源


def setting():
    print("setting")
    GlobalVariable.set_value('flag_show_humiture', not GlobalVariable.get_value('flag_show_humiture'))
    print('##############flag_show_humiture',GlobalVariable.get_value('flag_show_humiture'))
    GlobalVariable.set_value('flag_show_setting', not GlobalVariable.get_value('flag_show_setting'))
    print('##############flag_show_setting', GlobalVariable.get_value('flag_show_setting'))


def down():
    print("down")
    GlobalVariable.set_value('temp_thres', GlobalVariable.get_value('temp_thres') - 1)


def up():
    print('up')
    GlobalVariable.set_value('temp_thres', GlobalVariable.get_value('temp_thres') + 1)


def button_input(sleep_count, sleeptime_for_gt):
    global buttons
    for i in range(sleep_count):
        # 有优先级之分
        if GPIO.input(setting_button) > 0:
            buttons[0] = 1
        elif GPIO.input(down_button) > 0:
            buttons[1] = 1
        elif GPIO.input(up_button) > 0:
            buttons[2] = 1
        time.sleep(sleeptime_for_gt)


async def detect_input():
    global buttons
    GPIO.setup(setting_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置setting_button管脚为输入模式，上拉至高电平(3.3V)
    GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置setting_button管脚为输入模式，上拉至高电平(3.3V)
    GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置setting_button管脚为输入模式，上拉至高电平(3.3V)
    # 中断函数，当轻触按键按下时，调用detect函数

    # GPIO.add_event_detect(setting_button, GPIO.BOTH, callback=setting_button_detect, bouncetime=200)
    # GPIO.add_event_detect(down_button, GPIO.BOTH, callback=down_button_detect, bouncetime=200)
    # 消抖处理，参考侯新源同学的想法，将每一秒分成20帧
    sleep_count = 20
    sleeptime = 0.5  # 0.5s一个操作
    sleepfactor = 1

    sleeptime_for_gt = float(sleeptime / sleep_count * sleepfactor)  # 1gt时间

    while True:
        # await
        buttons = [0, 0, 0]  # 每次循环都要刷新一遍
        button_input(sleep_count, sleeptime_for_gt)
        if buttons[0] == 1:
            setting()
        elif buttons[1] == 1:
            down()
        elif buttons[2] == 1:
            up()
        await asyncio.sleep(0.2)
    # while True:
    #
    #     print(GPIO.input(setting_button), GPIO.input(down_button))
    #     if GPIO.input(setting_button) > 0:
    #         print(f"setting button")
    #     if GPIO.input(down_button) > 0:
    #         print(f"up buttons")
    #     time.sleep(0.1)


# 程序入口
if __name__ == '__main__':
    makerobo_setup()  # 初始化GPIO口
    print('start')
    detect_input()
    # try:
    #     makerobo_loop()  # 循环函数
    # except KeyboardInterrupt:  # 当按下Ctrl+C时，将执行destroy()子程序。
    #     makerobo_destroy()  # 资源释放
