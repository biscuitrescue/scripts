#!/usr/bin/env python3

from subprocess import run
from sys import argv
from shutil import copyfile
from os.path import exists

themes = {
    "Everforest": {
        "openbox": "Everforest-Openbox",
        "qtile": "everforest",
        "nvim": "everforest",
        "Gtk": "Everforest-Dark-B",
        "kitty": "everforest",
        "polybar": "everforest",
        "alacritty": "palenight",
        "emacs": "everforest",
        "zathura": "everforest",
        "waybar": "everforest"
    },
    "Tam": {
        "openbox": "Latte-Openbox",
        "qtile": "latte",
        "nvim": "gruvbox",
        "Gtk": "Catppuccin-Latte",
        "kitty": "tam",
        "polybar": "tam",
        "alacritty": "catppuccin",
        "emacs": "latte",
        "zathura": "latte",
        "waybar": "latte"
    },
    "Latte": {
        "openbox": "Latte-Openbox",
        "qtile": "latte",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-Latte",
        "kitty": "latte",
        "polybar": "latte",
        "alacritty": "catppuccin",
        "emacs": "latte",
        "zathura": "latte",
        "waybar": "latte"
    },
    "Macchiato": {
        "openbox": "Macchiato-Openbox",
        "qtile": "macchiato",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-Macchiato",
        "kitty": "macchiato",
        "polybar": "macchiato",
        "alacritty": "catppuccin",
        "emacs": "macchiato",
        "zathura": "macchiato",
        "waybar": "macchiato"
    },
    "Frappe": {
        "openbox": "Frappe-Openbox",
        "qtile": "frappe",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-Frappe",
        "kitty": "frappe",
        "polybar": "frappe",
        "alacritty": "catppuccin",
        "emacs": "frappe",
        "zathura": "frappe",
        "waybar": "frappe"
    },
    "Mocha": {
        "openbox": "Mocha-Openbox",
        "qtile": "mocha",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-Mocha",
        "kitty": "mocha",
        "polybar": "mocha",
        "alacritty": "catppuccin",
        "emacs": "mocha",
        "zathura": "mocha",
        "waybar": "mocha"
    },
    "Purple": {
        "openbox": "Purple-Openbox",
        "qtile": "purple",
        "nvim": "palenight",
        "Gtk": "Nordic-darker-v40",
        "kitty": "purple",
        "polybar": "purple",
        "alacritty": "dracula",
        "emacs": "purple",
        "zathura": "dracula",
        "waybar": "mocha"
    },
    "Dracula": {
        "openbox": "Dracula-withoutBorder",
        "qtile": "dracula",
        "nvim": "dracula",
        "Gtk": "Dracula-pink-accent",
        "kitty": "dracula",
        "polybar": "dracula",
        "alacritty": "dracula",
        "emacs": "doom-dracula",
        "zathura": "dracula",
        "waybar": "dracula"
    },
    "Palenight": {
        "openbox": "Palenight-Openbox",
        "qtile": "palenight",
        "nvim": "palenight",
        "Gtk": "palenight",
        "kitty": "palenight",
        "polybar": "palenight",
        "alacritty": "palenight",
        "emacs": "doom-palenight",
        "zathura": "palenight",
        "waybar": "palenight"
    },
    "One": {
        "openbox": "Doom-One",
        "qtile": "one",
        "nvim": "doom-one",
        "Gtk": "AtomOneDarkTheme",
        "kitty": "one",
        "polybar": "one",
        "alacritty": "one",
        "emacs": "doom-one",
        "zathura": "macchiato",
        "waybar": "palenight"
    },
    "Nord": {
        "openbox": "Nord-Openbox",
        "qtile": "nord",
        "nvim": "nord",
        "Gtk": "Nordic-darker-v40",
        "kitty": "nord",
        "polybar": "nord",
        "alacritty": "one",
        "emacs": "doom-nord",
        "zathura": "macchiato",
        "waybar": "palenight"
    },
    "Rosepine": {
        "openbox": "Macchiato-Openbox",
        "qtile": "rosepine",
        "nvim": "rose-pine",
        "Gtk": "Rosepine-Moon-BL",
        "kitty": "rosepinemoon",
        "polybar": "macchiato",
        "alacritty": "one",
        "emacs": "macchiato",
        "zathura": "rose-pine",
        "waybar": "macchiato"
    }
}


thing = {
    'openbox': ((42, (10, -8)), '.config/openbox/rc.xml'),
    'qtile': ((7, (9, -2)), '.config/qtile/screens.py'),
    'kitty': ((-1, (15, -6)), '.config/kitty/kitty.conf'),
    # 'alacritty': ((-1, (33, -5)), '.config/alacritty/alacritty.yml'),
    'Gtk': ((1, (15, -1)), '.config/gtk-3.0/settings.ini'),
    'polybar': ((0, (40, -5)), '.config/polybar/config.ini'),
    'nvim': ((-2, (12, -1)), '.config/nvim/init.vim'),
    'emacs': ((34, (18, -2)), '.doom.d/config.el'),
    'zathura': ((-1, (8,-1)), '.config/zathura/zathurarc'),
    'waybar': ((0, (9,-7)), '.config/waybar/style.css')
}


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


theme = argv[-1]

theme = theme.capitalize()

a = run(
    'echo $HOME',
    shell=True,
    text=True,
    capture_output=True
)

home = a.stdout.strip()+'/'

if theme not in themes:
    print("Error: Theme not found")
    exit()

obj = list(thing)

for i in obj:
    switch_theme(i, theme)

if theme in ['Mocha', 'Macchiato', 'Frappe', 'Latte']:
    with open(f'{home}{thing["nvim"][1]}', 'r') as f:
        x = f.readlines()
    old = x[-7][15:-2]
    new = x[-7].replace(old, theme.lower())
    x[-7] = new

    with open(f'{home}{thing["nvim"][1]}', 'w') as w:
        for i in x:
            w.write(i)
run(
    f'gsettings set org.gnome.desktop.interface gtk-theme {themes[theme]["Gtk"]}',
    shell=True
)

if exists(f".themes/{themes[theme]['Gtk']}/gtk-4.0/gtk.css"):
    copyfile(f".themes/{themes[theme]['Gtk']}/gtk-4.0/gtk.css", ".config/gtk-4.0/gtk.css")

run(
    'qtile cmd-obj -o cmd -f reload_config',
    shell=True
)
run(
    'openbox --reconfigure',
    shell=True
)
run(
    'killall waybar && waybar &',
    shell=True
)
