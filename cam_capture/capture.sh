#!/bin/bash
while true
do
	DATE=$(date +"%Y-%m-%d_%H%M")
	raspistill -o $HOME/logs/pics/$DATE.jpg
	echo $HOME/logs/pics/$DATE.jpg
	sleep 60
done
