from discord.ext import commands


class MiscellaneousCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def changelog(self, ctx):
        await ctx.message.channel.send(
            "This is a changelog"
        )

    @commands.command()
    async def killbot(self, ctx):
        """
        Turns the bot off
        :param ctx: Context class from Discord.py
        :return:
        """
        message = ctx.message
        if message.author.id == 169896955298709505:
            await message.channel.send("Goodbye! {}".format(self.client.get_emoji(455209722719633408)))
            await self.client.close()
        else:
            await message.channel.send("You are not my master!")

    @commands.command()
    async def goodbot(self, ctx):
        """
        Filler command. Bot sends a message on call.
        :param ctx: Context class from Discord.py
        :return: None
        """
        message = ctx.message
        await message.channel.send("ty fam {}".format(self.client.get_emoji(568167721532129301)))

    @commands.command()
    async def badbot(self, ctx):
        """
        Same as goodbot
        """
        message = ctx.message
        await message.channel.send(self.client.get_emoji(521430122503471114))
        await message.channel.send(self.client.get_emoji(521430137724731392))

    @commands.command()
    @commands.cooldown(1, 60)
    async def com(self, ctx):
        """
        Alternative to .help from Discord.py
        Worse implementation due to being hardcoded
        :param ctx:  ontext class from Discord.py
        :return: None
        """
        message = ctx.message
        await message.channel.send(
            "==Copypasta==\n"
            ".addpasta <key> \"<contents>\" = add a copypasta triggered by typing <key> in chat\n"
            ".eatpasta <key> = remove a copypasta, requires admin permission\n"
            "\n==Reactions==  \"19.04.2019\"\n"
            ".adreact <key> <emote> = bot will react with <emote> messages containing <key>\n"
            ".rmreact <key> = remove a reaction activated by <key>\n"
            "\n==Reddit==\n"
            ".rtop <subreddit> = top post from <subreddit> \n" +
            ".rrand <subreddit> = random reddit post from <subreddit> \n" +
            ".rrsearch <keywords> = random reddit search of a <keywords> \n" +
            ".rsearch <keywords> = first search result of <keywords>from reddit \n"
            "\n==Youtube==\n"
            ".randyt <keywords> = random search result of <keywords> from youtube \n" +
            ".yt <keywords> = first result of <keywords> from youtube \n"
            "\n==Other==\n"
            ".goodbot \n" +
            ".badbot \n"
            ".killbot\n"
        )


def setup(bot):
    """
    Required for the functionality of cog
    :param bot: commands.Bot
    :return: None
    """
    bot.add_cog(MiscellaneousCog(bot))
