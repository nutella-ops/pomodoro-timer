#!/usr/bin/python3
import time, os

n = 0
while(1):
    userInput = input("[" + str(n) + "] minutes: ")
    minutes = float(userInput)
    time.sleep(minutes * 60)
    for y in userInput:
        os.system("ffplay -nodisp -autoexit ~/work_a*/git*/pomo*/res/"+y+"-1.wav 1>/dev/null 2>/dev/null")
    if userInput == 0.5 or 0.10 or 0.15 or 0.20:
        n += 0
    else:
        n += 1