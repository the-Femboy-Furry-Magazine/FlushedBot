import discord
import platform
import random
import requests
import json

import bot_data
import commands


class FlushedClient(discord.Client):
    async def send_message(self, message, channel):
        channel = client.get_channel(channel.id)
        await channel.send(message)

    async def guild_id_get(self):
        for guild in client.guilds:
            guild_id = guild
            return guild_id
        
    async def filter_slur(self, message, channel, guild, slur):
        global slurred
        guild_id = guild
        mod_channel = discord.utils.get(guild_id.channels, name="flushedbot-logs")
        await message.delete()
        try:
            await FlushedClient.send_message(self, f"Slur was filtered"
                                                   f"\nSent by {message.author}"
                                                   f"\nMessage: {message.content}"
                                                   f"\nOffending slur: {slur}", mod_channel)
        except AttributeError:
            await FlushedClient.send_message(self, "ERROR: A #flushedbot-logs channel does not exist!"
                                                   "\nPlease make sure that a #flushedbot-logs channel exists in your"
                                                   " server!", channel)

    async def send_log(self, message, channel, guild):
        guild_id = guild
        mod_channel = discord.utils.get(guild_id.channels, name="flushedbot-logs")
        try:
            await FlushedClient.send_message(self, message, mod_channel)
        except AttributeError:
            await FlushedClient.send_message(self, "ERROR: A #flushedbot-logs channel does not exist!"
                                             "\nPlease make sure that a #flushedbot-logs channel exists in your"
                                             " server!", channel)

    async def kick_user(self, message, user: discord.Member, user2: discord.Member, *, reason="KICKED BY FLUSHEDBOT: no reason provided", channel):
        await FlushedClient.send_log(self, f"{user.name} was kicked\nReason: KICKED BY {user2} USING FLUSHEDBOT: {reason}", channel, message.guild)
        await user.kick(reason=f"KICKED WITH FLUSHEDBOT: {reason}")

    async def ban_user(self, message, user: discord.Member, user2: discord.Member, *, reason="BANNED BY FLUSHEDBOT: no reason provided", channel):
        await FlushedClient.send_log(self, f"{user.name} was banned\nReason: BANNED BY {user2} USING FLUSHEDBOT: {reason}", channel, message.guild)
        await user.ban(reason=f"BANNED WITH FLUSHEDBOT: {reason}")

    async def check_for_commands(self, message, channel, ctx=None):
        mod_length = len(bot_data.moderators)
        i = 0
        while i != mod_length:
            if bot_data.moderators[i] in f"{message.author.id}":
                author_is_mod = True
            else:
                author_is_mod = False
            i += 1

        command = message.content
        if not command.startswith(bot_data.BOT_PREFIX):
            return

        command = command.removeprefix(bot_data.BOT_PREFIX)
        command_args = command.split(" ")

        if command_args[0] in commands.command_map:
            commands.command_map[command_args[0]](self, {
                "message": message,
                "channel": channel
            })
        elif message.content.startswith(bot_data.BOT_PREFIX):
            await FlushedClient.send_message(self, f"Unknown command \"{command}\"", channel)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            print(f'Bot said {message.content}')
        elif message.author != self.user:
            print(f'Message from {message.author}: {message.content}')
            slur = commands.has_slur(message.content)
            if not slur:
                await FlushedClient.check_for_commands(self, message, message.channel)
            else:
                await FlushedClient.filter_slur(self, message, message.channel, message.guild, slur)


intents = discord.Intents.default()
intents.message_content = True

client = FlushedClient(intents=intents)
