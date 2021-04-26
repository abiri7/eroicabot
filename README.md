# eroicabot
A discord bot built with Python. Demonstration: https://youtu.be/1wZFne4X2G4

The biggest difficulty in making this bot was actually trying to get it up 24/7. Making it so that heroku could actually deploy our bot was a challenge - specifically the requirements.txt file that is needed for the bot to be to deployed. We ultimately found out that there was a way to auto-generate the requirements file and with a few minor version tweaks (we ended up lowering the versions for some of the requirements as it generated versions that sometimes didn't make much sense).

One thing we both learned was a lot of the stuff in the Discord.py documentation (https://discordpy.readthedocs.io/en/latest/) as well as commands to update our bot whenever we need to do so (ie. git add . ; git commit -am "insert commit note" ; git push heroku master)

The most fun aspect of this was actually figuring out what went wrong each and every time our bot died. Also noticing the fun little things that we didn't know before, such as the fact that the .py file can actually be run while the bot is hosted by heroku, and the bot will just reply back with the same message twice.
