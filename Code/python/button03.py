#!/usr/bin/env python3
import pygame
import signal
import sys
import RPi.GPIO as GPIO

screen = pygame.display.set_mode((1920, 1080))
screen.fill((255, 255, 255))
pygame.display.flip()

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_pressed_callback(channel):
        global q
        global z
        global y
        
        if GPIO.input(4) == 0:
            print("4 pressed!")
            z = 15
            q = 30  
        if GPIO.input(14) == 0:
            print("14 pressed!")
            z = 20
            q = 40
        if GPIO.input(15) == 0:
            print("15 pressed!")
            z = 10
            q = 20
        if GPIO.input(17) == 0:
            print("17 pressed!")
            z = 40
            q = 80
        if GPIO.input(18) == 0:
            print("18 pressed!")
            z = 45
            q = 90
        if GPIO.input(27) == 0:
            print("27 pressed!")
            z = 35
            q = 70
        if GPIO.input(22) == 0:
            print("22 pressed!")
            z = 30
            q = 60
        if GPIO.input(23) == 0:
            print("23 pressed!")
            z = 25
            q = 50
        if GPIO.input(24) == 0:
            print("24 pressed!")
            z = 65
            q = 130
        if GPIO.input(10) == 0:
            print("10 pressed!")
            z = 70
            q = 140
        if GPIO.input(9) == 0:
            print("9 pressed!")
            z = 60
            q = 120
        if GPIO.input(25) == 0:
            print("25 pressed!")
            z = 55
            q = 110
        if GPIO.input(11) == 0:
            print("11 pressed!")
            z = 50
            q = 100
            
        screen.fill((255, 255, 255))
        for x in range(0,60):
            y = x*q
            pygame.draw.rect(screen, (0, 0, 0), (0 ,y ,1920 ,z))
        pygame.display.flip()
            
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(4, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(14, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(15, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(17, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(18, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(27, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(22, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(23, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(24, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(10, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(9, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(25, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(11, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    
