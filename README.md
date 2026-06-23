# PipVideoController
This repository holds the bridge.py file required for my PipVideoController Holotape and walks you through the setup and operation of this holotape.


To use the PipVideoController holotape, you need to have a few things on your computer. 

First, go download python 3.14.5 as this was the version of python the bridge.py file was written in.
Python Download link: https://www.python.org/downloads/release/python-3145/

Next, download the bridge.py file directly from this repository.

After those steps, you now need to set up the bridge to match your computer. Its different for everybody so please pay close attention otherwise it will not work for you. 

Plug your pip-boy into your pc.

Right click on the windows logo at the bottom middle or bottom left of your screen and on that menu, select device manager.

In device manager, look for the "Ports (COM & LPT) drop down menu.

Expand that menu and find the active USB Serial Device. Beside it you will see "COM" with a number beside it.

For example, Mine says USB Serial Device (COM4). 

After you have your pip boy's port, find the bridge.py file you downloaded, right click it, go to "Edit in IDLE", then click "Python 3.14.5.

This will open a python code editor for the bridge.py. 

At the top of the code, you will see "SERIAL_PORT = 'YOURCOMHERE'

Replace "YOURCOMHERE" with your com number. For me it would be COM4 so it would say SERIAL_PORT = 'COM4'

After doing that, go to the top left of the python code editor, click file, and click save.

You should now have your bridge.py setup correctly.

Now, we need to set up the holotape to properly play the videos.

Open your file explorer, Click This PC > OS (C:).

Right click in the empty area, and make a new folder, and name it "VIDEO" in all caps.

Put all of your videos you wish to play, in this folder.

Im too lazy to type the rest of this so watch the video below to figure out how to set up each video in the holotape.

Also, one last thing. When adding a song to your holotape, BE SURE YOU FIND EVERY BACKSLASH AND DOUBLE THEM LIKE I DID IN THE VIDEO.

If you dont, then the video wont play and the command prompt will throw an error. Pasted below is the layout to use for adding more videos


use this one if you add a new one to the list

{ name: "YOURVIDEONAME", path: "YOURVIDEOPATH"},

Use this one if its the FINAL video in the list

{ name: "YOURVIDEONAME", path: "YOURVIDEOPATH"}

Below is the tutorial video.


[![Watch the video](https://img.youtube.com/vi/OJcgd73h0-c/0.jpg)](https://youtu.be/OJcgd73h0-c)

