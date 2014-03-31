import os
import shutil
import sys
from subprocess import call

usbno = sys.argv[1]
rootPath = '/media/usb'+usbno

with open('/proc/mounts','r') as content_file:
  mounts = content_file.read()

mounted = mount.upper().find(rootPath.upper())

if mounted > 0:
  os.system('rm -r '+rootPath+'/*')
  os.system('dd if=/dev/zero of='+rootPath+'/file_1TB bs=1M oflag=noatime')
  os.remove(rootPath+'/file_1TB')
