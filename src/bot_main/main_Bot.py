from discord.ext import commands
from classified.bot_token.token import bot_token
from src.commands.copypasta.EventFunction import copypasta_on_msg
from src.commands.Reactions.EventFunction import react_to_msg

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    """
    Runs when bot starts / connects to Discord
    :return: None
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_disconnect():
    """
    Runs when bot gets shut down
    :return: None
    """
    print("Bot has logged off")


@client.event
@commands.cooldown(1, 20)
async def on_message(message):
    """
    Discord.py function. On message sent in any discord channel/server
    :param message: Message object from Discord.py
    :return: None
    """

    if message.author == client.user:
        return
    # if message.author.id == 244573404059926529:
    #     return
    # log_chat("chatlogs", message)

    await react_to_msg(message, client)
    await copypasta_on_msg(message)

    # if message.content.lower().startswith('hello') or message.content.lower().startswith("hey"):
    #     await message.channel.send('Hello {} !'.format(message.author.mention))
    #     return
    await client.process_commands(message)


# LOAD COGS

client.load_extension("src.commands.BotMiscellaneous.cog")
client.load_extension("src.commands.Youtube.cog")
client.load_extension("src.commands.Reddit.cog")
client.load_extension("src.commands.Dictionary.cog")
client.load_extension("src.commands.Reactions.cog")
client.load_extension("src.commands.copypasta.cog")
client.load_extension("src.commands.DiscordVoice.cog")
client.load_extension("src.commands.RateGirl.cog")
client.run(bot_token)

# DONE Create the class for reactions triggered by keywords
# STUPIDTODO create the class for bot messages that start with
# TODO make bot save images
# TODO MAKE bot play music - bot can currently join/leave channels - postponed until bot is hosted
# TODO HOST BOT on a server
