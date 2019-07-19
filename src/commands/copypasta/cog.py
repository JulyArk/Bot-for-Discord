from discord.ext import commands
from src.commands.copypasta.controller import CopyPastaController


class CopyPastaCog(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        #self.controller = CopyPastaController(bot.ctx.guild)

    @commands.command()
    async def addpasta(self, ctx):
        """
        Add response to keyword
        Adds a:
        -Bot responds with a message(also known as a copypasta, thus the name)
        once a key message is sent in the discord.
        Requires:
         -Admin rights to add a message
        :param ctx: Context class from Discord.py
        :return: None
        """
        message = ctx.message
        if message.author.id == 169896955298709505 or message.author.id == 514151264016400384:
            pasta_controller = CopyPastaController(ctx.guild)
            print(pasta_controller.get_dict())
            status = pasta_controller.add(message.content)
            if status == -1:
                await message.channel.send("Error: 3 < all fields < 250")
            elif status == 0:
                await message.channel.send("pasta already exists")
            else:
                await message.channel.send("Added!")
            return

        if not message.author.top_role.permissions.administrator:
            await message.channel.send("You have no power here")
            return
        pasta_controller = CopyPastaController(ctx.guild)
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
        controller = CopyPastaController(ctx.guild)
        message = ctx.message
        if message.author.top_role.permissions.administrator \
                or message.author.id == 169896955298709505 or message.author.id == 514151264016400384:  # backdoor
            msg = controller.remove(message.content)
            if msg == 1:
                await message.channel.send("Removed!")
                print(message.author.id)
            elif msg == -1:
                await message.channel.send("Not found")
            elif msg == 0:
                await message.channel.send("Bad input")
            return
        else:
            await message.channel.send("You have no power here")

    # @commands.command()
    # async def update_addpasta_9432585699(self, ctx):
    #     try:
    #         CopyPastaController().update_to_access_bits()
    #         await ctx.channel.send("Successsfully updated!")
    #     except Exception:
    #         await ctx.channel.send("Something went wrong!")

    @commands.command()
    async def pastabits(self, ctx):
        message = " ".join(ctx.message.content.split()[1:])
        result = CopyPastaController(ctx.guild).set_bits(message)
        if result:
            await ctx.channel.send("Successfully Updated!")
            return
        await ctx.channel.send("Key not found!")


def setup(bot):
    bot.add_cog(CopyPastaCog(bot))
