import os
from sys import stdout
from time import sleep
stdout.write("[=18h")
os.system("clear")

screen = os.get_terminal_size()
for char in range(screen.lines):
    for char in range(screen.columns):
        stdout.write("[44m ")
    stdout.flush()
for char in range(screen.columns):
    stdout.write("[A")
    stdout.flush()
sleep(3)
stdout.write("[37mHi bro wassup")
stdout.flush()
sleep(10)
