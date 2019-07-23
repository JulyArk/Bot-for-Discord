from src.commands.copypasta.controller import CopyPastaController
import time

last_used_time = 0  # A global cooldown time


async def copypasta_on_msg(message):
    """
    Used to check if the message is  copy pasta.
    Full implementation in copypasta
    :param message: Discord.py message Class
    :return: None
    """
    global last_used_time  # Load global
    # Admins get to dodge the cooldown
    if not message.author.top_role.permissions.administrator:
        # If user is not an admin and triggers a copypasta during the cooldown stop executing
        if last_used_time + 15 > time.time():
            return
        else:  # Refresh cooldown
            last_used_time = time.time()
    pasta_controller = CopyPastaController(message.guild)  # Load the controller
    # pasta_controller.pastas.import_guild_pastas("copypastas_pickle.txt") # this is here if you need imports
    if message.content in pasta_controller.pastas.pasta_dict:  # If the message is in the dict keys
        contents = pasta_controller.get_dict()[message.content]  # Found
        if contents[1] == 1:  # If bits for the copypasta are set to 1 remove the trigger message
            await message.delete()
        #   print(pasta_controller.get_dict())
        await message.channel.send(contents[0])  # Print the copypasta
        return
