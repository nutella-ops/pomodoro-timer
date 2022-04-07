#!/usr/bin/python3
import time, os

def day():
    print(time.ctime()[4:10])

def clk():
    print(time.ctime()[11:19])

file = time.ctime()[4:19]

n = 0
day()
print("-----------")
while(1):
    clk()
    userInput = input("[" + str(n) + "] minutes: ")
    minutes = float(userInput)
    time.sleep(minutes * 60)
    for y in userInput:
        os.system("ffplay -nodisp -autoexit ~/work_a*/git*/pomo*/res/"+y+"-1.wav 1>/dev/null 2>/dev/null")
    n += 1
    os.system("echo " + time.ctime()[4:19] + " >> /tmp/" + "'" + file + "'" + ".txt")
