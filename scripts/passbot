#!/usr/bin/env bash

mkdir -p ~/mountpts/password/

sudo cryptsetup open /dev/disk/by-uuid/7fbfe937-372a-4b65-a7ac-0afe56870f40 pass-bot
sudo mount /dev/mapper/pass-bot ~/mountpts/password
cp ~/mountpts/password/key_big.txt ~/PASSBOT/lev_big/key.txt
cp ~/mountpts/password/key_smol.txt ~/PASSBOT/lev_smol/key.txt
echo "Passbot is ready you have 10 minutes until it locks up"

sleep 600

rm ~/PASSBOT/lev_big/key.txt
rm ~/PASSBOT/lev_smol/key.txt
  
sudo umount ~/mountpts/password
sudo cryptsetup close /dev/mapper/pass-bot
sudo eject /dev/disk/by-uuid/7fbfe937-372a-4b65-a7ac-0afe56870f40 

echo "Done"

sudo rm -rf ~/mountpts/password/
lsblk

