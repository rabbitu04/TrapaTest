# TrapaTest
Create a discord bot.

What this bot can do:
 - echo: Repeat input.
 - kick: Kick user. (Need a role with permission)
 - ban: Ban user. (Need a role with permission)
 - text_channel: Create a channel with name you want.
 - broadcast: Let the bot send message to specified channel at specified time. (Using crontab setting style) The jobs will be deleted once you stop the python script.

Set up steps (on windows 11 with powershell):
 1. Create an discord bot. Please refer to https://discordpy.readthedocs.io/en/stable/discord.html
 2. Clone the repo to your local dir or somewhere you like to run it.
 3. Create a virtual env under the directory and install packages needed. I use<br />
 `python3 -m venv venv` and run `pip install -r requirements.txt` after getting into virtual env.
 4. Set environment variable `TOKEN`. You can get it when you create your discord bot.<br />
 Edit `/path_to_dir/venv/Scripts/Activate.ps1` in my case.
 5. Edit `constants.py` if needed. You can set configs of roles and command prefix in it.
 6. Get into the virtual env and run the bot with `python my_trapa_bot.py`.
