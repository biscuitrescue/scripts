#!/usr/bin/env python3

from subprocess import run
from sys import argv
from shutil import copyfile
from os.path import exists


a = run(
    'echo $HOME',
    shell=True,
    text=True,
    capture_output=True
)

home = a.stdout.strip() + '/'


def find_nvim():
    with open(f"{home}.config/nvim/init.lua") as f:
        x = f.readlines()
    for i in x:
        if "background" in i:
            return x.index(i)


def switch_theme(obj, theme):
    with open(f'{home}{thing[obj][1]}', 'r') as f:
        x = f.readlines()
    line = thing[obj][0][0]
    ind = thing[obj][0][1]

    old = x[line][ind[0]:ind[1]]
    new = x[line].replace(old, themes[theme][obj])

    x[line] = new
    with open(f'{home}{thing[obj][1]}', 'w') as w:
        for i in x:
            w.write(i)


themes = {
    "Dark": {
        "nvim": "dark",
        "alacritty": "hojicha",
        "kitty": "hojicha",
        "rofi": "ashes",
        "starship": "kanagawa",
        "waybar": "ink"
    },
    "Light": {
        "nvim": "light",
        "alacritty": "latte",
        "kitty": "latte",
        "rofi": "latte",
        "starship": "catppuccin_latte",
        "waybar": "canvas"
    },
}


thing = {
    'nvim': ((find_nvim(), (18, -2)), '.config/nvim/init.lua'),
    'alacritty': ((-1, (38, -8)), '.config/alacritty/alacritty.toml'),
    'kitty': ((-1, (15, -6)), '.config/kitty/kitty.conf'),
    'rofi': ((-1, (8, -2)), '.config/rofi/config.rasi'),
    'starship': ((0, (11, -2)), '.config/starship.toml'),
    'waybar': ((0, (16, -7)), '.config/waybar/style.css'),
}

theme = argv[-1]

theme = theme.capitalize()

if theme not in themes:
    print("Error: Theme not found")
    exit()

obj = list(thing)

for i in obj:
    switch_theme(i, theme)

run(
    'makoctl reload',
    shell=True
)
