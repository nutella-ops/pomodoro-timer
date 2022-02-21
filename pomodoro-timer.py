#!/usr/bin/python3
import time, os

n = 0
while(1):
    minutes = input("[" + str(n) + "] minutes: ")
    time.sleep(float(minutes) * 60)
    for y in minutes:
        os.system("ffplay -nodisp -autoexit ~/work_a*/git*/pomo*/res/"+y+"-1.wav 1>/dev/null 2>/dev/null")
    n += 1