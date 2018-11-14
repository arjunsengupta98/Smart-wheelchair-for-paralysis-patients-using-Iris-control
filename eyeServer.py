import curses
import RPi.GPIO as GPIO   
import RPi.GPIO as GPIO
import time
import os
from socket import *


host = "192.168.43.46"
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 

TRIG = 17
ECHO = 27
led = 22

m11=16
m12=12
m21=21
m22=20

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(led,GPIO.OUT)                  

GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)

GPIO.output(led, 1)

time.sleep(5)

def stop():
    print "stop"
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print "Forward"

def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print "back"

def right():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print "right"

def left():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print "left"
stop()
while True:
	

	print "Waiting to receive messages..."
	(data, addr) = UDPSock.recvfrom(buf)
	#print "Received message: " + data
	#print(data)
	
	if data == "forward":
		print("forward")
		forward()
	elif data == "right":
		print("right")
		right()
	elif data == "left":
		print("left")
		left()
UDPSock.close()

os._exit(0) 

		















