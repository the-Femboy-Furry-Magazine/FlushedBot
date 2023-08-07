import bot_data
import platform
import random


async def has_slur(message):
    for slur in bot_data.slurs:
        if slur in message:
            return slur
    else:
        return False


async def cmd_info(flushed_client, arg: dict):
    channel = arg.get("channel")
    await flushed_client.send_message(
                            f"FlushedBot version {bot_data.version}"
                            f"\n{bot_data.github_link}"
                            f"\n----------------------------"
                            f"\nBot made by p866e"
                            f"\nRunning on a(n) {platform.system()} {platform.release()} host"
                            f"\nPython version {platform.python_version()}",
                            channel)
    return


async def cmd_ping(flushed_client, arg: dict):
    channel = arg.get("channel")
    await flushed_client.send_message(f"pong! {flushed_client.latency}ms", channel)


async def cmd_help(flushed_client, arg: dict):
    channel = arg.get("channel")
    await flushed_client.send_message(
                            f"```"
                            f"Commands:\n(prefix is \"{bot_data.BOT_PREFIX}\")\n"
                            f"\ninfo                   Tells you info about the bot"
                            f"\nping                   Gets the bot's latency"
                            f"\n8ball                  Asks a question to the mighty 8-ball"
                            f"\nhelp                   Displays info about commands"
                            f"\nban                    Bans a user (mod only)"
                            f"\nkick                   Kicks a user (mod only)"
                            f"\nuwu                    Gives you a random uwu emote"
                            f"\nbk                     The last thing you'd want in your Burger King burger-"
                            f"\nversiontree            shows the versions of FlushedBot, and what they added"
                            f"\necho                   Echos your message"
                            f"\nrate                   Rates your message on a scale of 1 to 10"
                            f"```", channel)


async def cmd_ban(flushed_client, arg: dict):
    message = arg.get("message")
    channel = arg.get("channel")
    if message.author.top_role.permissions.administrator:
        message_args = message.content
        message_args = message_args.split(" ", 2)
        member = message_args[1]
        try:
            await flushed_client.ban_user(message, message.mentions[0], message.author, reason=message_args[2],
                                       channel=channel)
        except IndexError:
            await flushed_client.ban_user(message, message.mentions[0], message.author,
                                           reason="No reason provided", channel=channel)
    if not message.author.top_role.permissions.administrator:
        await flushed_client.send_message("You do not have permission to use this command.", channel)


async def cmd_kick(flushed_client, arg: dict):
    message = arg.get("message")
    channel = arg.get("channel")
    if message.author.top_role.permissions.administrator:
        message_args = message.content
        message_args = message_args.split(" ", 2)
        print(message_args)
        member = message_args[1]
        try:
            await flushed_client.kick_user(message, message.mentions[0], message.author, reason=message_args[2],
                                       channel=channel)
        except IndexError:
            await flushed_client.kick_user(message, message.mentions[0], message.author,
                                           reason="No reason provided", channel=channel)
    if not message.author.top_role.permissions.administrator:
        await flushed_client.send_message("You do not have permission to use this command.", channel)


async def cmd_uwu(flushed_client, arg: dict):
    channel = arg.get("channel")

    random_index = random.randint(0, len(bot_data.uwu_emotes) - 1)

    await flushed_client.send_message(f"{bot_data.uwu_emotes[random_index]}", channel)


async def cmd_bk(flushed_client, arg: dict):
    channel = arg.get("channel")
    await flushed_client.send_message(f"Number 15: Burger king foot lettuce. The last thing you'd want in your Burger "
                                      f"King burger is someone's foot fungus. But as it turns out, that might be what "
                                      f"you get. A 4channer uploaded a photo anonymously to the site showcasing his "
                                      f"feet in a plastic bin of lettuce. With the statement: \"This is the lettuce "
                                      f"you eat at Burger King.\" Admittedly, he had shoes on.",
                                      channel)


async def cmd_versiontree(flushed_client, arg: dict):
    channel = arg.get("channel")
    await flushed_client.send_message(f"Version tree:\n\n"
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
                                      f"\n--------------------- FlushedBot overhaul"
                                      f"\n0.4                 Added a bunch of shit. See the GitHub commits for the "
                                      f"changes that 0.4 made so far"
                                      f"\n```",
                                      channel)


async def cmd_echo(flushed_client, arg: dict):
    message = arg.get("message")
    channel = arg.get("channel")
    message_content = message.content
    message_content = message_content.split(" ", 1)
    await flushed_client.send_message(f"{message_content[1]}", channel)


async def cmd_rate(flushed_client, arg: dict):
    message = arg.get("message")
    channel = arg.get("channel")
    message_arg = message.content
    message_arg = message_arg.split(" ", 1)
    rate_goodyness = random.randint(1, 4)
    if rate_goodyness == 1 or rate_goodyness == 2:
        await flushed_client.send_message(f"{message.author} wants to rate: {message_arg[1]}"
                                               f"\nThe bot rates it a {random.randint(10, 20) // 2}/10.", channel)
    if rate_goodyness == 3 or rate_goodyness == 4:
        await flushed_client.send_message(f"{message.author} wants to rate: {message_arg[1]}"
                                               f"\nThe bot rates it a {random.randint(1, 20) // 2}/10.", channel)
    return


command_names = [
    "info",
    "ping",
    "help",
    "ban",
    "kick",
    "uwu",
    "bk",
    "versiontree",
    "echo",
    "rate"
]
command_map = {
    "info": cmd_info,
    "ping": cmd_ping,
    "help": cmd_help,
    "ban": cmd_ban,
    "kick": cmd_kick,
    "uwu": cmd_uwu,
    "bk": cmd_bk,
    "versiontree": cmd_versiontree,
    "echo": cmd_echo,
    "rate": cmd_rate,
}

command_help = {
    "info": f"Usage: {BOT_PREFIX}help\nGives you info about the bot\nNo arguments required",
    "ping": f"Usage: {BOT_PREFIX}ping\nRetrieves uptime about the bot\nNo arguments required",
    "help": f"Usage: {BOT_PREFIX}help [command]\nGives you info about the bot\nNo arguments needed, but 1 optional argument is avaliable",
    "ban": f"Usage: {BOT_PREFIX}ban [user] [reason]\nBans a player from the server\n1 argument is required, but the 2nd is optional\nAdministrator only",
    "kick": f"Usage: {BOT_PREFIX}ban [user] [reason]\nKicks a player from the server\n1 argument is required, but the 2nd is optional\nAdministrator only",
    "uwu": f"Usage: {BOT_PREFIX}help\nGives you a random ASCII unicode\nNo arguments required",
    "bk": f"Usage: {BOT_PREFIX}help\nnumber 15\nNo arguments required",
    "versiontree": f"Usage: {BOT_PREFIX}versiontree\nGives you an outline of the versions of FlushedBot\nNo arguments required",
    "echo": f"Usage: {BOT_PREFIX}echo [message]\nRepeats what you say\nArgument is required",
    "rate": f"Usage: {BOT_PREFIX}rate [something]\nRates something on a 1-10 scale.\nArgument is required",
}