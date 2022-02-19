#!/usr/bin/env python3
import os

from datetime import date
with open(".status.txt") as file:
  x=file.read().strip()
L=x.split(":")

dtoday=str(date.today())

if L[0]==dtoday and L[1]=="Y":
  print("Your system has been updated atleast once today")
else:
  print("Your system has not been updated today")
  resp = input("Would you like to update right now? [Y/n]: ")
  if resp=="Y" or resp=="y" or resp=='':
    os.system("sudo pacman -Syu --noconfirm")
    with open(".status.txt","w"):
      file.write(dtoday+":Y")
    print("Your system has been updated")
  else:
    print("Please update whenever you are free")

    
