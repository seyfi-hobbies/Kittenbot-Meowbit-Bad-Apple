# Bad Apple on Kittenbot Meowbit using MicroPython (No sound)

## Screenshot:
![](https://github.com/seyfi-hobbies/Kittenbot-Meowbit-Bad-Apple/blob/main/images/IMG-3911.PNG)

For a quick weekend project I implemented Bad Apple on a kid's game console, Meowbit.

To see it in action see the YouTube video here: https://www.youtube.com/watch?v=jnb9CIecFG8


Meowbit is a card-sized graphical retro game computer with allows you coding with Makecode arcade and Python. 

Since the device has 2MB flash memory Bad Apple frames couldn't be stored there, so I used an SD card to store video and code.
In fact if you install Micropython to your Meowbit and copy the SD-card.zip into the root of an SD card you can run the program immediately without running Micropython IDE. 

## Install MicroPython
I copied MicroPython UF2 (meowbit.uf2) into Meowbit's root directory. See the details here: https://www.kittenbot.cc/blogs/learn/meowbit-micropython-programming

MicroPython mounts the SD card automatically and starts running main.py found in the root folder of SD card.
The Python code is very simple. Just display the frames one by one. To improve the speed I need to skip some of the frames instead of reducing the image size or video size.

```python
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
```

## Bad Apple Frames
I found Every Bad Apple frames on Github in PNG format. Somehow MicroPython on Meowbit doesn't support PNG display so I needed to convert those frames to BMP format. There is a Python Utility file in the util/ folder used once on Windows.
