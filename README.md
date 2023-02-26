# Bad Apple on Kittenbot Meowbit using MicroPython (No sound)

## Screenshot:
![In-Game](https://raw.githubusercontent.com/seyfi-hobbies/Kittenbot-Meowbit-Bad-Apple/main/images/MicroPython.png)
https://raw.githubusercontent.com/seyfi-hobbies/Kittenbot-Meowbit-Bad-Apple/main/images/IMG-3913.png

For a quick weekend project I implemented Bad Apple on a kid's game console, Meowbit.

To see it in action see the YouTube video here: https://www.youtube.com/watch?v=jnb9CIecFG8


Meowbit is a card-sized graphical retro game computer with allows you coding with Makecode arcade and Python. 

Since the device has 2MB flash memory Bad Apple frames couldn't be stored there, so I used an SD card to store video and code.
In fact if you install Micropython to your Meowbit and copy the SD-card.zip into the root of an SD card you can run the video immediately. 

## Install MicroPython
I copied MicroPython UF2 (meowbit.uf2) into Meowbit's root directory. See the details here: https://www.kittenbot.cc/blogs/learn/meowbit-micropython-programming

MicroPython mounts the SD card automatically and starts running main.py found in the root folder of SD card.
The code is very simple. Just display the frames one by one. To improve the speed I need to skip some of the frames instead of reducing the image size or video size.

## Bad Apple Frames
I found Every Bad Apple frames on Github in PNG format. Somehow MicroPython on Meowbit doesn't support PNG display so I needed to convert those frames to BMP format. There is a Python Utility file in the source used once on Windows.
