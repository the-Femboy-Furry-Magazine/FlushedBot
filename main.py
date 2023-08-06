import discord
import os
import platform
import random
import requests
import json


BOT_PREFIX = "f!"
slurs = ["nigg", "xigg", "fag", "trann"]
moderators = ["1", "873014876275114005"]
eightballanswers = ["Yes", "Indubitably", "Outlook good", "Do more thinking and try again.", "Don't count on it.",
                    "My sources say no.", "Ask again later.", "Cannot predict now.", "404",
                    "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start." ]
uwuemotes = ["owo", "OwO", "uwu", "UwU", ">w<", ">~<", "~<~", ">O<", ":3" ]
servmods = [ "1" ]
slurred = False
version = "0.35-beta"
github_link = "https://github.com/AcousticallyAutistic/FlushedBot/"


def get_servers():
    global servers
    servers = requests.get("classicube.net/api/servers")
    servers = json.loads(servers.text)
    print("servers gotten")
    print(servers['servers'][1])

class MyClient(discord.Client):
    async def sendMessage(self, message, channel):
        channel = client.get_channel(channel.id)
        await channel.send(message)

    async def guildIdGet(self):
        for guild in client.guilds:
            guildid = guild
            return guildid
    async def slurCheck(self, message, channel, guild):
        global slurred
        guild_id = guild
        slurmessage = f"{message.content}"
        slurmessage = slurmessage.lower()
        print(slurmessage)
        slurs_length = len(slurs)
        i = 0
        slurred = False
        while i != slurs_length:
            if slurs[i] in slurmessage:
                modchannel = discord.utils.get(guild_id.channels, name="flushedbot-logs")
                await message.delete()
                try:
                    await MyClient.sendMessage(self, f"Slur was filtered"
                                                     f"\nSent by {message.author}"
                                                     f"\nMessage: {message.content}"
                                                     f"\nOffending slur: {slurs[i]}", modchannel)
                    slurred = True
                except AttributeError:
                    await MyClient.sendMessage(self, "ERROR: A #flushedbot-logs channel does not exist!"
                                                     "\nPlease make sure that a #flushedbot-logs channel exists in your"
                                                     " server!", channel)
                    slurred = True
            i += 1
        return

    async def sendLog(self, message, channel, guild):
        guild_id = guild
        modchannel = discord.utils.get(guild_id.channels, name="flushedbot-logs")
        try:
            await MyClient.sendMessage(self, message, modchannel)
        except AttributeError:
            await MyClient.sendMessage(self, "ERROR: A #flushedbot-logs channel does not exist!"
                                             "\nPlease make sure that a #flushedbot-logs channel exists in your"
                                             " server!", channel)

    async def kickUser(self, message, user: discord.Member, user2: discord.Member, *, reason="KICKED BY FLUSHEDBOT: no reason provided", channel):
        await MyClient.sendLog(self, f"{user.name} was kicked\nReason: KICKED BY {user2} USING FLUSHEDBOT: {reason}", channel, message.guild)
        await user.kick(reason=f"KICKED BY FLUSHEDBOT: {reason}")

    async def banUser(self, message, user: discord.Member, user2: discord.Member, *, reason="BANNED BY FLUSHEDBOT: no reason provided", channel):
        await MyClient.sendLog(self, f"{user.name} was banned\nReason: BANNED BY {user2} USING FLUSHEDBOT: {reason}", channel, message.guild)
        await user.ban(reason=f"BANNED BY FLUSHEDBOT: {reason}")

    async def checkForCommands(self, message, channel, ctx=None):
        mod_length = len(moderators)
        i = 0
        while i != mod_length:
            if moderators[i] in f"{message.author.id}":
                authorIsMod = True
            else:
                authorIsMod = False
            i += 1

        if message.content.startswith(BOT_PREFIX + "info"):
            await MyClient.sendMessage(self, f"FlushedBot version {version}"
                                             f"{github_link}"
                                             f"\n----------------------------"
                                             f"\nBot made by p866e"
                                             f"\nRunning on a(n) {platform.system()} {platform.release()} host"
                                             f"\nPython version {platform.python_version()}", channel)
            return

        if message.content.startswith(BOT_PREFIX + "ping"):
            await MyClient.sendMessage(self, f"pong! {self.latency}ms", channel)
            return

        if message.content.startswith(BOT_PREFIX + "help") or message.content.startswith(BOT_PREFIX + "cmds")or message.content.startswith("<@1130529530663141397>"):
            await MyClient.sendMessage(self, f"```"
                                             f"Commands:\n(prefix is \"{BOT_PREFIX}\")\n"
                                             f"\ninfo                   Tells you info about the bot"
                                             f"\nping                   Gets the bot's latency"
                                             f"\n8ball                  Asks a question to the mighty 8-ball"
                                             f"\nhelp                   Displays info about commands"
                                             f"\nban                    Bans a user (mod only)"
                                             f"\nkick                   Kicks a user (mod only)"
                                             f"\nuwu                    Gives you a random uwuemote"
                                             f"\nbk                     Gives you the famous foot lettuce copypasta"
                                             f"\nverstree/versiontree   shows the versions of FlushedBot, and what they added"
                                             f"\necho                   Echos what you said"
                                             f"\nrate                   Rates a thing on a scale of 1 to 10"
                                             f"```", channel)
            return

        if message.content.startswith(BOT_PREFIX + "verstree") or message.content.startswith(BOT_PREFIX + "versiontree"):
            await MyClient.sendMessage(self, f"Version tree:\n\n"
                                             f"```"
                                             f"\n0_testing           added help/cmds, info"
                                             f"\n0.1                 added 8ball"
                                             f"\n0.2                 added ban, kick, ping"
                                             f"\n0.3                 added uwu, bk"
                                             f"\n0.31                added verstree/versiontree"
                                             f"\n0.32                added echo, modified info"
                                             f"\n0.33                modified help"
                                             f"\n0.34                added rate"
                                             f"\n0.35-beta           i forgot what i added"
                                             f"\n```", channel)
            return

        if message.content.startswith(BOT_PREFIX + "8ball"):
            messagecontent = message.content
            messagecontent = messagecontent.split(" ", 1)
            randomanswer = random.randint(0, len(eightballanswers)-1)
            if "go fuck yourself" in messagecontent[1]:
                await MyClient.sendMessage(self, f"{message.author} asked the 8ball: {messagecontent[1]}"
                                                 f"\nThe 8-ball answers: How about YOU go fuck yourself!", channel)
                return

            await MyClient.sendMessage(self, f"{message.author} asked the 8ball: {messagecontent[1]}"
                                             f"\nThe 8-ball answers: {eightballanswers[randomanswer]}", channel)
            return

        if message.content.startswith(BOT_PREFIX + "kick"):
            if message.author.top_role.permissions.administrator == True:
                messagecontent = message.content
                messagecontent = messagecontent.split(" ", 2)
                member = messagecontent[1]
                await MyClient.kickUser(self, message, message.mentions[0], message.author, reason=messagecontent[2], channel=channel)
            if message.author.top_role.permissions.administrator == False:
                await MyClient.sendMessage(self, "You can't use this command!", channel)
            return

        if message.content.startswith(BOT_PREFIX + "ban"):
            if message.author.top_role.permissions.administrator == True:
                messagecontent = message.content
                messagecontent = messagecontent.split(" ", 2)
                member = messagecontent[1]
                await MyClient.banUser(self, message, message.mentions[0], message.author, reason=messagecontent[2], channel=channel)
            if message.author.top_role.permissions.administrator == False:
                await MyClient.sendMessage(self, "You can't use this command!", channel)
            return

        if message.content.startswith(BOT_PREFIX + "uwu"):
            messagecontent = message.content
            messagecontent = messagecontent.split(" ", 1)
            randomanswer = random.randint(0, len(uwuemotes)-1)
            await MyClient.sendMessage(self, f"{uwuemotes[randomanswer]}", channel)
            return

        if message.content.startswith(BOT_PREFIX + "bk"):
            await MyClient.sendMessage(self, f"Number 15: Burger king foot lettuce. The last thing you'd want in your Burger King burger is someone's foot fungus. But as it turns out, that might be what you get. A 4channer uploaded a photo anonymously to the site showcasing his feet in a plastic bin of lettuce. With the statement: \"This is the lettuce you eat at Burger King.\" Admittedly, he had shoes on.", channel)
            return

        if message.content.startswith(BOT_PREFIX + "echo"):
            messagecontent = message.content
            messagecontent = messagecontent.split(" ", 1)
            await MyClient.sendMessage(self, f"{messagecontent[1]}", channel)
            return

        if message.content.startswith(BOT_PREFIX + "rate"):
            messagecontent = message.content
            messagecontent = messagecontent.split(" ", 1)
            rate_goodyness = random.randint(1,4)
            if rate_goodyness == 1 or rate_goodyness == 2:
                await MyClient.sendMessage(self, f"{message.author} wants to rate: {messagecontent[1]}"
                                                 f"\nThe bot rates it a {random.randint(10, 20)//2}/10.", channel)
            if rate_goodyness == 3 or rate_goodyness == 4:
                await MyClient.sendMessage(self, f"{message.author} wants to rate: {messagecontent[1]}"
                                                 f"\nThe bot rates it a {random.randint(1, 20)//2}/10.", channel)
            return

        if BOT_PREFIX in message.content:
            messagecontent = message.content
            messagecontent = messagecontent.split("f!", 1)
            try:
                await MyClient.sendMessage(self, f"Unknown command \"{messagecontent[1]}\"", channel)
            except IndexError:
                await MyClient.sendMessage(self, f"Empty command", channel)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.author == self.user:
            print(f'Bot said {message.content}')
        elif message.author != self.user:
            print(f'Message from {message.author}: {message.content}')
            await MyClient.slurCheck(self, message, message.channel, message.guild)
            print(slurred)
            if slurred is False:
                await MyClient.checkForCommands(self, message, message.channel)
            elif slurred is True:
                return

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTEzMDUyOTUzMDY2MzE0MTM5Nw.Gjxysb.1LqtcphINeJMNxy0LOQ4OrNbJG6itQt90yB7Bk')
