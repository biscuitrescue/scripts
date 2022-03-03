#!/usr/bin/env python3
import subprocess
a=subprocess.Popen(['dunstctl', 'is-paused'], stdout=subprocess.PIPE)
out=a.communicate()
x=out[0].decode().strip()
if x=='true':
    subprocess.run('dunstctl set-paused false', shell=True)
    subprocess.run("notify-send 'Notifications back on'", shell=True)
elif x=='false':
    subprocess.run('dunstctl set-paused true', shell=True)