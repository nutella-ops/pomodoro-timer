#!/usr/bin/python3
import time, os

day = time.ctime()[4:10]

n = 0
while(1):
    userInput = input("[" + str(n) + "] minutes: ")
    minutes = float(userInput)

    startTime = time.ctime()[11:16]
    time.sleep(minutes * 60)
    stopTime = time.ctime()[11:16]

    logEntry = startTime + " -- " + stopTime
    print(day + " " + logEntry)

    os.system("ffplay -nodisp -autoexit $(find ~ -name 'g.wav' 2>/dev/null) 2>/dev/null")
    n += 1
    os.system("echo " + logEntry + " >> /tmp/" + "'" + day + "'" + ".txt")
