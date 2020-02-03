# Raspberri Pi 3B+   As   Camera

##  Step 1: install OpenCV  (Link for tutorail required)

##  Step 2:copy camera.py into your desktop

## Step 3: create startup-pointer
open your terminal and insert following command :
$ cd /etc/xdg/autostart
$ sudo nano startPiCamera.desktop

fill the "startPiCamera.desktop" with following text: 
[Desktop Entry]
Name=runCamera
Type=Application
Exec=sh /usr/bin/runCamera.sh
Terminal=false


press Ctrl+X and save it 

then run follwoing commands:

$ sudo nano /usr/bin/runCamera.sh

insert follwoing commands in the nano editor: 


#!/bin/sh/
cd /home/pi/Desktop
python3 camera.py &

press Ctrl+X and save the file
now you can restart your raspberry and your code will automatically executed as Desktop is booted


configuration steps are described in this [youtube video] (https://www.youtube.com/watch?v=yDJgohRfTb0)
