from src.commands.Reactions.controller import ReactionsController


async def react_to_msg(message, client):
    """
    Used to check message contents for keywords. Adds a specified reaction on a message.
    Full implementation in Reactions
    :param message: Discord.py Message class
    :param client: bot from commands.Bot
    :return: None
    """
    reaction_controller = ReactionsController(client, message.guild)
    # reaction_controller.react_dict.import_guild_reactions("reactions_pickle.txt") # if you need to import reacts
    dict_r = reaction_controller.get_dict()
    for key in dict_r:
        if message.content.find(key) != -1:
            await message.add_reaction(client.get_emoji(dict_r[key]))
            return
