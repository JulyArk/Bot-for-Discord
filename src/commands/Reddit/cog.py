# REDDIT
from discord.ext import commands
from src.commands.Reddit.post_from_subreddit import RedditBot


class RedditCog(commands.Cog):
    """
    Cog for reddit class, searches for certain results on reddit using the praw library
    """

    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def rsearch(self, ctx):
        """
        Returns the top post from reddit for a topic (a word or multiple words)
        Prohibits nsfw posts from appearing in non-nsfw channels
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return:None
        """
        message = ctx.message
        topic = " ".join(ctx.message.content.split()[1:])
        is_nsfw, url = RedditBot().search_first_topic(" ".join(topic))
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))

    @commands.command()
    async def rrand(self, ctx):
        """
        Random search result from a subreddit
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message

        subreddit = ctx.message.content.split()[1]
        is_nsfw, url = RedditBot().random_post_sub(subreddit)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))

    @commands.command()
    async def rtop(self, ctx):
        """
        Top post from the hot section of a certain subreddit, ignoring pinned messages
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message
        subreddit = ctx.message.content.split()[1]
        is_nsfw, url = RedditBot().top_post_subreddit(subreddit)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))
                await message.add_reaction(self.client.get_emoji(521430137724731392))

    @commands.command()
    async def rrsearch(self, ctx):
        """
        Random search result of a post from reddit using a keyword/s
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message

        topic = " ".join(ctx.message.content.split()[1:])
        is_nsfw, url = RedditBot().search_topic_random(topic)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))


def setup(bot):
    bot.add_cog(RedditCog(bot))
