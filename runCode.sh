#!/bin/bash

sleep 0.1
loop=1
while [loop]
do
	if xhost >& /dev/null ; then loop=0
	fi
	sleep 0.1
done

startx /home/pi/main.py -- -nocursor &

