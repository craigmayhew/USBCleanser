import os
import shutil
import sys
import RPi.GPIO as GPIO
from subprocess import call

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)

usbno = sys.argv[1]
rootPath = '/media/usb'+usbno

with open('/proc/mounts','r') as content_file:
  mounts = content_file.read()

mounted = mount.upper().find(rootPath.upper())

if mounted > 0:
  GPIO.setup(7, GPIO.OUT)
  GPIO.output(7, True)
  os.system('rm -r '+rootPath+'/*')
  os.system('dd if=/dev/zero of='+rootPath+'/file_1TB bs=1M oflag=noatime')
  os.remove(rootPath+'/file_1TB')

GPIO.output(7, False)
