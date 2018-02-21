# Import Libraries
import os
import time
from gpiozero import LED, Button, Buzzer

# Set up variables for the LED, Buzzer and switch pins
drive_red = LED(18)
drive_yellow = LED(23)
drive_green = LED(24)
button = Button(25)
buzzer = Buzzer(22)
walk_red = LED(20)
walk_green = LED(21)

def carsDrive():
    drive_green.on()
    walk_red.on()

def carsSlow():
    drive_green.off()
    drive_yellow.on()
    time.sleep(5)

def carsStop():
    drive_yellow.off()
    drive_red.on()
    walk_red.off()
    walk_green.on()
    for i in range(0,9):
        buzzer.on()
        time.sleep(0.5)
        buzzer.off()
        time.sleep(0.5)

def walkerWarning():
    walk_green.off()
    buzzer.off()
    for i in range(0,5):
        walk_red.on()
        time.sleep(0.5)
        walk_red.off()
        time.sleep(0.5)
    walk_red.on()

def ignoreButton():
    drive_green.on()
    time.sleep(20)

while True:
    carsDrive()
    if button.ispressed:
        carsSlow()
        carsStop()
        walkerWarning()
        ignoreButton()
