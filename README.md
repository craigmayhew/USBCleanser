USBCleanser
===========

Scripts to turn a debian based OS (including raspberry pi) into an automated USB wiper.

The intended use of these scripts are to make an automated device that securely wipes data from USB drives that are plugged into it.

Instructions For Debian Jessie
============

 - sudo apt-get install usbmount ntfs-3g
 - Place dataObliterator.py in /home/pi/
 - Place etc/systemd/system/usbmount@.service in /etc/systemd/system/usbmount@.service
 - Place etc/udev/rules.d/usbmount.rules in /etc/udev/rules.d/usbmount.rules


Instructions For Debian Before Jessie
============

 - sudo apt-get install usbmount
 - Place dataObliterator.py in /home/pi/
 - Place 01_wipe_data in /etc/usbmount/mount.d/01_wipe_data
 - chmod 755 /etc/usbmount/mount.d/01_wipe_data

ToDo
====

Turn this into a single, simple package.

Further Reading
============
http://raspberrypi.stackexchange.com/questions/41959/automount-various-usb-stick-file-systems-on-jessie-lite
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=774149
https://www.freedesktop.org/software/systemd/man/systemd.service.html
