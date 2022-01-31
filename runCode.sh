#!/bin/bash

sleep 0.1
FILE=started
if test -f "$FILE"; then
  rm started
fi

while [ 1 ]
do
#python3 main.py
startx /home/pi/main.py -- -nocursor &
if test -f "$FILE"; then
echo "File exists"
break

else 
echo "No File"
fi

sleep 1
done