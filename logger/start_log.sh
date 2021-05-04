#!/bin/bash

session="log"

session_exists=$(tmux list-sessions | grep $log)

if [ "$session_exists" != "" ]
then
    read -p "Do you wish to kill current session [N/y] " yn
    if [[ $yn == [Yy]* ]]
    then
        tmux kill-session -t $session
    else
        /bin/sleep 15
        exit
    fi
fi

# Only create tmux session if it doesn't already exist
if [ "$session_exists" = "" ]
then
    
    tmux new-session -d -s $session

    tmux new-window -n 'camera'
    tmux send-keys -t 'camera' "./../capture/capture.sh" C-m
    
    tmux new-window -n 'altimeter'
    tmux send-keys -t 'altimeter' 'python ../altimeter/altimeter.py' C-m

    tmux new-window -n 'gps'
    tmux send-keys -t 'gps' 'python ../gps/gps.py' C-m

	

    tmux select-window -t ''
fi

exit 0

