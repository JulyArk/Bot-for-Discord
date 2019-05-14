from src.commands.copypasta.controller import CopyPastaController


async def copypasta_on_msg(message):
    """
    Used to check if the message is  copy pasta.
    Full implementation in copypasta
    :param message: Discord.py message Class
    :return: None
    """
    pasta_controller = CopyPastaController()
    if message.content in pasta_controller.pastas.pasta_dict:
        await message.channel.send(pasta_controller.get_dict()[message.content])
        return
