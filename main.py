import discord
import os
import platform
import random
import requests
import json


import bot_data
print(bot_data.startup)

import discord_client



with open("bot_token.txt", "r") as bot_token_file:
    bot_token = bot_token_file.read()
    bot_token_file.close()

discord_client.client.run(bot_token)
