# Mooncraft Alpha
Reads Minecraft chat in the DECTalk TTS heard in Moonbase Alpha.
## Dependancies
[Python](https://www.python.org/downloads/)
[PythMC](https://github.com/MrKelpy/PythMC) (pip install pythmc)
[DECTalk](https://github.com/dectalk/dectalk) (download "vs6.zip" from the releases page)
## Installation
Once you've downloaded the above dependancies and the .py file, move "MooncraftAlpha.py" into it's own folder, then create a new folder alongside it called "dectalk" and move the files from the DECTalk download into it.
## Tips & Known Issues
Wait until at-least 1 chat message has been sent before starting the program, otherwise it will crash because it won't be able to find a log file.\n
Clients that change the log file location won't work with this program. As far as I know, this is a limitation with PythMC.\n
The program may crash with a "can't decode byte" error. This is another bug with PythMC. To fix this, go to your .minecraft appdata folder, open "logs" then delete "latest.log".\n
The volume of the speech can not be adjusted or streamed easily. A workaround for this is to type a really long message, change the output of the say.exe program to go through a program like [Virtual Audio Cable](https://vb-audio.com/Cable/), then use another program to monitor the audio.\n
