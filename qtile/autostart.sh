#!/bin/sh
#Audio
pulseaudio --start &
sleep 5 &
pulseaudio -k &
killall pulseaudio &
pulseaudio --start &

#icons of system
udiskie -t &
nm-applet &
nitrogen --restore &
