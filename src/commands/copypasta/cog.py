from discord.ext import commands
from src.commands.copypasta.controller import CopyPastaController


class CopyPastaCog(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def addpasta(self, ctx):
        """
        Bot responds with a message for a keyword/s
        Adds a:
        -Bot responds with a message(also known as a copypasta, thus the name)
        once a key message is sent in the discord.
        Requires:
         -Admin rights to add a message
        :param ctx: Context class from Discord.py
        :return: None
        """
        message = ctx.message
        if not message.author.top_role.permissions.administrator:
            await message.channel.send("You have no power here")
            return
        pasta_controller = CopyPastaController()
        status = pasta_controller.add(message.content)
        if status == -1:
            await message.channel.send("Error: 3 < all fields < 250")
        elif status == 0:
            await message.channel.send("pasta already exists")
        else:
            await message.channel.send("Added!")

    @commands.command()
    async def eatpasta(self, ctx):
        """
        Removes one of the copypastas
        :param ctx: Context class from Discord.py
        :return: None
        """
        controller = CopyPastaController()
        message = ctx.message
        if message.author.top_role.permissions.administrator:
            msg = controller.remove(message.content)
            if msg == 1:
                await message.channel.send("Removed!")
            elif msg == -1:
                await message.channel.send("Not found")
            elif msg == 0:
                await message.channel.send("Bad input")
        else:
            await message.channel.send("You have no power here")


def setup(bot):
    bot.add_cog(CopyPastaCog(bot))
