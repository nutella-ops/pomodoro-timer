#!/usr/bin/python3
import time, numpy as np, simpleaudio as sa


def beep(frequency, seconds):
    fs = 44100  # 44100 samples per second

    # Generate a sine wave
    note = np.sin(frequency * np.linspace(0, seconds, seconds * fs, False) * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs) 
    time.sleep(0.1)

    # Wait for playback to finish before exiting
    play_obj.wait_done() 

def lowsound(times):
    while times > 0: 
        beep(332, 1)
        times -= 1

def hisound(times):
    while times > 0: 
        beep(574, 1)
        times -= 1

def alarm(lo, hi):
    lowsound(lo)
    hisound(hi)


def metaalarm(times, lo, hi):
    while times > 0: 
        alarm(lo, hi)
        times -= 1
while(1):
    time.sleep(float(input("minutes (float): ")) * 60)
    metaalarm(15, 1, 1)
