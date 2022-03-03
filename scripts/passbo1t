#!/usr/bin/env bash

mkdir -p ~/mountpts/key
stuff=$(ls ~/mountpts/password)

while true; do
    read -p "Do you want to mount usb [Y/N]" choice
    case $choice in
        [nN]*)
            break
            ;;
        [yY]*)
            read -p 'Name for mapper: ' name
            sudo mount /dev/mapper/name
            exit 1
            ;;
        *)
            echo "Invalid, please choose again">&2
    esac
done

if [ -z "$stuff" ]; then
  sudo cryptsetup open /dev/disk/by-uuid/7fbfe937-372a-4b65-a7ac-0afe56870f40 pass-bot
  sudo mount /dev/mapper/pass-bot ~/mountpts/password
  cp ~/mountpts/password/key_big.txt ~/PASSBOT/lev_big/key.txt
  cp ~/mountpts/password/key_smol.txt ~/PASSBOT/lev_smol/key.txt
  echo "Passbot is ready you have 5 minutes until it locks up"
  sleep 30
  rm ~/PASSBOT/lev_big/key.txt
  rm ~/PASSBOT/lev_smol/key.txt
  
  sudo umount ~/mountpts/password
  sudo cryptsetup close /dev/mapper/pass-bot
  sudo eject /dev/disk/by-uuid/7fbfe937-372a-4b65-a7ac-0afe56870f40 
else
  sudo umount ~/mountpts/password
  sudo cryptsetup close /dev/mapper/pass-bot
  sudo eject /dev/disk/by-uuid/7fbfe937-372a-4b65-a7ac-0afe56870f40 

fi

echo "Done"
lsblk

