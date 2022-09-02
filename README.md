# TrapaTest
Create a discord bot.

What this bot can do:
 - echo: repeat input.
 - kick: kick user. (Need a role with permission)
 - ban: ban user. (Need a role with permission)
 - text_channel: create channel with name you want.
 - broadcast: let the bot send message to specified channel at specified time. (Using crontab setting style)

Set up steps (on windows 11 with powershell):
 1. Create an discord bot. Please refer to https://discordpy.readthedocs.io/en/stable/discord.html
 2. Clone the repo to your local dir or somewhere you like to run it.
 3. Create a virtual env under the directory. I use<br />
 `python3 -m venv venv`
 4. Set environment variable `TOKEN`. You can get it when you create your discord bot.<br />
 Edit `/path_to_dir/venv/Scripts/Activate.ps1` in my case.
 5. Edit `constants.py` if needed. You can set configs of roles and command prefix in it.
 6. Get into the virtual env and run the bot with `python my_trapa_bot.py`.
