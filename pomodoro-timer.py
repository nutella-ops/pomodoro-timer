#!/usr/bin/python3
import time, os

while(1):
    minutes = input("minutes (float): ")
    time.sleep(float(minutes) * 60)
    for y in minutes:
        os.system("ffplay -nodisp -autoexit ~/work_a*/git*/pomo*/res/"+y+"-1.wav")
