#!/bin/bash

path=../logs/
time=10
while getopts f:t: flag
do
    case "${flag}" in
        f) path=${OPTARG};;
		t) time=${OPTARG};;
    esac
done

echo "Path: $path";
echo "Interval: $time";


while true
do
	DATE=$(date +"%Y-%m-%d_%H%M%S")
	fullpath=$path$DATE.jpg
	raspistill -o $fullpath
	echo $fullpath
	sleep $time
done
