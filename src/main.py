#/bin/python

from meowbit import *
import os

x = 1
screen.sync = 0
while True:
    screen.loadBmp('{:04d}/frame{:05d}'.format(int(x/1000)*1000,x)+'.bmp',0,0)
    screen.refresh()
    x += 5
    if x > 6505:
        x=1