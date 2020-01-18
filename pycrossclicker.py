# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PyCrossClicker - Fully customizable python console application            #
# Copyright (C) 2019 TrackRunny                                             #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os

divider = "————————————————————————————————————————————————————————"

try:
    clicks = float(input("Delay speed: (Default: 0.060 Seconds ~ 15 Clicks Per Second): "))
    delay = clicks
except ValueError:
    clicks = 0.060
    delay = clicks

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_start_and_stop_key = str(input("Start And Stop Key: (Default: x): "))
start_stop_key = KeyCode(char=input_start_and_stop_key)

if input_start_and_stop_key == "":
    start_stop_key = KeyCode(char="x")

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_exit_key = str(input("Exit Key: (Default: `): "))
exit_key = KeyCode(char=input_exit_key)

if input_exit_key == "":
    exit_key = KeyCode(char="`")

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————

input_button = str(input("Options: Left, Right, Middle"
                         "\nMouse button: (Default: Left Mouse Button): "))
input_button = input_button.lower()
button = Button.left

if input_button == "right":
    button = Button.right
elif input_button == "middle":
    button = Button.middle
else:
    pass

print(divider)

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


print("Clicker is ready!")

# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————
# ———————————————————————————————————————————————————————


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            os.system("clear")
            print("Clicking as stopped!")
            print(divider)
        else:
            click_thread.start_clicking()
            os.system("clear")
            print("Clicking as started!")
            print(divider)
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
