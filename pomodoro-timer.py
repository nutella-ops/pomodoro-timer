#!/usr/bin/python3
import time, os

def dayCheck():
    if (sysTime[2] == day):
        os.system("echo " + logPom + " >> /tmp/" + fileName)
    else:
        print("new day")

sysTime = time.ctime().split()
day = sysTime[2]
month = sysTime[1]
dayLow = (month + day).lower()
fileName = dayLow +".txt"
dayMonth = month + " " + day

os.system("echo " + logHeader + " >> /tmp/" + fileName)

n = 0
while(1):
    userInput = input("[" + str(n) + "] minutes: ")
    minutes = float(userInput)

    startTime = sysTime[3][0:5]
    time.sleep(minutes * 60)
    stopTime = sysTime[3][0:5]

    logPom = startTime + ", " + stopTime
    print(logHeader + ", " + logPom)

    os.system("ffplay -nodisp -autoexit $(find ~ -name 'g.wav' 2>/dev/null) 2>/dev/null")
    n += 1

    if
    os.system("echo " + logHeader + " >> /tmp/" + fileName)


