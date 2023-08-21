# Simple dice rolling Telegram bot
## Installation
Copy the code to your local machine and cd to the directory
```commandline
git clone https://www.github.com/reirose/headswithrollbot.git
cd .\headswithrollbot
```
Install dependencies
```commandline
pip install python-telegram-bot
```
Now, you are ready to start the bot
```commandline
python main.py --token TELEGRAM BOT TOKEN
```
## Available commands:
 - ```/roll [n]d[m]``` -- roll _n_ d<i>m</i> dices.\
  Available dices: d4, d6, d8, d10, d12, d20, d100\
  E.g.: ```/roll 3d6 1d20```\
  Just ```/roll``` will roll you 1d100
 - ```/reroll``` -- reroll last dices