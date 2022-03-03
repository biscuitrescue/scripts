#!/usr/bin/env bash

mic(){
	inp=`pamixer --list-sources | awk '/alsa_input/ {printf $1}'`
	mic=`pamixer --source $inp --get-volume-human`
	if [[ "$mic" == "muted" ]]; then
		notify-send "Mic has been unmuted";
		pactl set-source-mute 0 toggle;
		sleep 2;
		dunstctl close-all;
	else
		pactl set-source-mute 0 toggle;
		# dunstctl close;
		notify-send "Mic has been muted";
		sleep 2;
		dunstctl close-all;
	fi
}

mic
