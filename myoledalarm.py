#!/usr/bin/python

# this is my script for my alarm to handle the oled display

import RPi.GPIO as GPIO
import sys, os, time, datetime, jason

class handleOLED():
  def __init__(self):
    super(handleOLED, self).__init__(name="handleOLED")
    
  
