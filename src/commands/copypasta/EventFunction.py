from src.commands.copypasta.controller import CopyPastaController
import time

last_used_time = 0


async def copypasta_on_msg(message):
    """
    Used to check if the message is  copy pasta.
    Full implementation in copypasta
    :param message: Discord.py message Class
    :return: None
    """
    global last_used_time
    if not message.author.top_role.permissions.administrator:
        if last_used_time + 15 > time.time():
            return
        else:
            last_used_time = time.time()
    pasta_controller = CopyPastaController(message.guild)
    # pasta_controller.pastas.import_guild_pastas("copypastas_pickle.txt") # this is here if you need imports
    if message.content in pasta_controller.pastas.pasta_dict:
        contents = pasta_controller.get_dict()[message.content]
        if contents[1] == 1:
            await message.delete()
        #   print(pasta_controller.get_dict())
        await message.channel.send(contents[0])
        return
