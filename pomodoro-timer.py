#!/usr/bin/python3
import time, os

sysTime = time.ctime().split()
day = sysTime[2]
month = sysTime[1]
dayLow = (month + day).lower()
fileName = dayLow +".txt"
logHeader = month + " " + time.ctime().split()[2]
os.system("echo " + logHeader + " >> /tmp/" + fileName)

def dayCheck():
    if (time.ctime().split()[2] == day):
        os.system("echo " + logPom + " >> /tmp/" + fileName)
    else:
        os.system("echo " + logHeader + " >> /tmp/" + fileName)
        os.system("echo " + logPom + " >> /tmp/" + fileName)

pom = 0
while(1):
    userInput = input("[" + str(pom) + "] minutes: ")
    minutes = float(userInput)

    startTime = time.ctime().split()[3][0:5]
    time.sleep(minutes * 60)
    stopTime = time.ctime().split()[3][0:5]
    os.system("ffplay -nodisp -autoexit $(find ~ -name 'g.wav' 2>/dev/null) 2>/dev/null")
    logPom = startTime + ", " + stopTime
    print(logHeader + ", " + logPom)
    dayCheck()
    pom += 1