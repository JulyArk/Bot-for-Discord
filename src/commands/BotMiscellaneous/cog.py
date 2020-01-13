from discord.ext import commands
import random
from bs4 import BeautifulSoup
import requests
import re
import urllib3
import urllib.request
import urllib.parse
import os
import argparse
import sys
import json
import time

votekick_on = 0


class MiscellaneousCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def changelog(self, ctx):
        await ctx.message.channel.send(
            "This is a changelog"
        )

    @commands.command(pass_context=True)
    async def lb(self, ctx):
        """
        Turn lb into kg (imperial to metric)
        :param ctx: Discord.py context
        :return: None
        """
        lb = float(ctx.message.content.split()[1])
        await ctx.channel.send("That is {0:.2f} kg".format(lb * 0.453592))

    @commands.command(pass_context=True)
    async def kg(self, ctx):
        """
        Turn kg into lb (metric to imperial)
        :param ctx:
        :return: None
        """
        lb = float(ctx.message.content.split()[1])
        await ctx.channel.send("That is {0:.2f} lbs".format(lb * 2.20462))

    @commands.command(pass_context=True)
    async def ft(self, ctx):
        """
        Turns height ft.inch (Eg: 5.11) to cm (imperial to metric)
        :param ctx: Discord.py context
        :return: None
        """
        value = float(ctx.message.content.split()[1])
        lb = int(value)
        inch = (value - int(value)) * 10
        cm = lb * 30.48 + inch * 2.54
        print(lb, inch)
        await ctx.channel.send("That is {0:.2f} cm".format(cm))

    @commands.command(pass_context=True)
    async def cm(self, ctx):
        """
        Turns cm (height) to ft + inch (metric to imperial) by approximation
        :param ctx: Discord.py context
        :return: None
        """
        value = float(ctx.message.content.split()[1])
        ft = int(value * 0.0328084)
        inch = round((value * 0.0328084 - ft) * 12)
        await ctx.channel.send("That is {}ft {}inches".format(ft, inch))

    @commands.command(pass_context=True)
    async def dice(self, ctx):
        """
        Rolls 2 dice ( returns 2 values between 1-6)
        :param ctx: Discord.py context
        :return: None
        """
        await ctx.channel.send(str(random.randint(1, 6)) + " " + str(random.randint(1, 6)))

    @commands.command()
    async def killbot(self, ctx):
        """
        Turns the bot off (admin only)
        :param ctx: Context class from Discord.py
        :return:
        """
        message = ctx.message
        if message.author.id == 169896955298709505 or message.author.id == 514151264016400384:
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

    @staticmethod
    def verify_vote(vote_list, new_vote):
        if new_vote not in vote_list:
            return True
        return False

    @commands.command()
    async def votekick(self, ctx):
        """
        Starts a votekick for a certain user, needs 51% votes
        :param ctx: Context
        :return: None
        """
        global votekick_on
        if votekick_on == 1:
            await ctx.channel.send("A votekick is already open")
            return
        votekick_on = 1
        voted = []  # list of user ID's that voted
        message = ctx.message  # message string
        user = message.content.split()[1]  # user mention
        votes_needed = 9  # int(len(message.guild.members) / 2 + 1)
        current_votes = 0
        await ctx.message.channel.send(
            "Starting a votekick for user {}."
            " Type \"vote yes\" or \"vote no\" \n"
            "Votes needed:({}/{}) "
                .format(user, current_votes, votes_needed))
        bot_message = None
        async for message in ctx.channel.history(limit=50):
            if message.author.name == "Iku-nee":
                bot_message = message
                break
        timer = 60
        current_timer = 0
        while current_timer < timer:
            time.sleep(1)
            async for message in ctx.channel.history(limit=50):
                if message.content == "vote yes":
                    if MiscellaneousCog.verify_vote(voted, message.author.id):
                        current_votes += 1
                        voted.append(message.author.id)

                    await bot_message.edit(
                        content="Starting a votekick for user {}."
                                " Type \"vote yes\" or \"vote no\" \n"
                                "Votes needed:({}/{})"
                            .format(user, current_votes, votes_needed))
                    await message.delete()
                elif message.content == "vote no":
                    voted.append(message.author.id)
                    await message.delete()

            current_timer += 1
        if current_votes >= votes_needed:
            await ctx.channel.send("The senate decision is exile, begone {}!".format(user))
        else:
            await ctx.channel.send("The senate spares {}".format(user))
        votekick_on = 0

    @commands.command()
    async def erase(self, ctx):
        """
        Erase N messages (admin only)
        :param ctx: Discord.py Context
        :return: None
        """
        message = ctx.message
        if not message.author.top_role.permissions.administrator:
            return
        await message.delete()
        value = int(message.content.split()[1])
        await ctx.channel.purge(limit=value)

    @staticmethod
    def find_number_in_str(data: str):
        """
        Finds all the numbers in a string and returns them concatenated
        Should only be used for Discord ID parsing !! It doesn't have much benefit besides that!
        :param data: A string
        :return: Integer, the number created
        """
        number = ""
        for char in data:
            if '0' <= char <= '9':
                number += char
        try:
            return int(number)
        except ValueError:
            return -1

    @commands.command()
    async def al(self, ctx):
        character = ctx.message.content.split()[1:]
        character = [word.lower().capitalize() if word.lower() != 'of' else word.lower() for word in character]
        await ctx.channel.send("https://azurlane.koumakan.jp/" + '_'.join(character))

    @commands.command()
    async def alwho(self, ctx):
        #   TODO proper web scraping
        character = ctx.message.content.split()[1:]
        character = [word.lower().capitalize() if word.lower() != 'of' else word.lower() for word in character]
        await ctx.channel.send(
            "https://azurlane.koumakan.jp/{}#/media/File:{}.png".format('_'.join(character), '_'.join(character)))

    @staticmethod
    def findAllNumbersInString(data: str):
        numberList = []
        number = ""
        for char in data:
            if '0' <= char <= '9':
                number += char
            elif number != "":
                numberList.append(int(number))
                number = ""
        if number != "":
            numberList.append(int(number))
            number = ""
        try:
            return numberList
        except ValueError:
            return -1

    @commands.command()
    async def hide(self, ctx):
        """
        Removes the messages of a user from a channel
        :param ctx: Discord.py Context
        :return: None
        """
        channel = ctx.channel
        if not ctx.message.author.top_role.permissions.administrator:
            return
        user = ctx.message.content.split()[1]  # raw user string name or nickname

        try:
            user_if_id = MiscellaneousCog.find_number_in_str(user)  # user id if given by pinging
        except ValueError:
            user_if_id = -1
        value = int(ctx.message.content.split()[2])  # number of messages to be deleted
        counter = 0  # messages found
        async for message in channel.history(limit=500):
            if counter == value:
                return
            if message.author.name == user or message.author.id == user_if_id:
                await message.delete()
                counter += 1

    @commands.command()
    async def avm(self, ctx):
        """
        Print avatar of pinged User
        :param ctx: Discord.py Context
        :return: None
        """
        author_id = self.find_number_in_str(ctx.message.content)
        for author in ctx.guild.members:
            if author.id == author_id:
                await ctx.channel.send(author.avatar_url)

    @commands.command()
    async def gimg(self, ctx):
        """
        Searcher for a random image from google
        :param ctx:
        :return:
        """

        text = " ".join(ctx.message.content.split()[1:])
        print(text)
        parser = argparse.ArgumentParser(description='Scrape Google images')
        parser.add_argument('-s', '--search', default=text, type=str, help='search term')
        parser.add_argument('-n', '--num_images', default=2, type=int, help='num images to save')
        parser.add_argument('-d', '--directory', default='/Users/gene/Downloads/', type=str, help='save directory')
        args = parser.parse_args()
        print(args)
        print(parser.description)
        query = args.search  # raw_input(args.search)
        print(query)
        # max_images = args.num_images
        # save_directory = args.directory
        # image_type = "Action"
        query = query.split()
        query = '+'.join(query)
        url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/43.0.2357.134 Safari/537.36"}
        soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), 'html.parser')
        ActualImages = []  # contains the link for Large original images, type of  image
        for a in soup.find_all("div", {"class": "rg_meta"}):
            link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            ActualImages.append((link, Type))
        # await ctx.channel.send(random.choice(ActualImages)[0])
        print(len(ActualImages))
        await ctx.channel.send(ActualImages[random.randint(0, len(ActualImages))][0])
    # @commands.command()
    # @commands.cooldown(1, 60)
    # async def com(self, ctx):
    #     """
    #     Alternative to .help from Discord.py
    #     Worse implementation due to being hardcoded
    #     :param ctx:  ontext class from Discord.py
    #     :return: None
    #     """
    #     message = ctx.message
    #     await message.channel.send(
    #         "==Copypasta==\n"
    #         ".addpasta <key> \"<contents>\" = add a copypasta triggered by typing <key> in chat\n"
    #         ".eatpasta <key> = remove a copypasta, requires admin permission\n"
    #         "\n==Reactions==  \"19.04.2019\"\n"
    #         ".adreact <key> <emote> = bot will react with <emote> messages containing <key>\n"
    #         ".rmreact <key> = remove a reaction activated by <key>\n"
    #         "\n==Reddit==\n"
    #         ".rtop <subreddit> = top post from <subreddit> \n" +
    #         ".rrand <subreddit> = random reddit post from <subreddit> \n" +
    #         ".rrsearch <keywords> = random reddit search of a <keywords> \n" +
    #         ".rsearch <keywords> = first search result of <keywords>from reddit \n"
    #         "\n==Youtube==\n"
    #         ".randyt <keywords> = random search result of <keywords> from youtube \n" +
    #         ".yt <keywords> = first result of <keywords> from youtube \n"
    #         "\n==Other==\n"
    #         ".goodbot \n" +
    #         ".badbot \n"
    #         ".killbot\n"
    #     )


def setup(bot):
    """
    Required for the functionality of cog
    :param bot: commands.Bot
    :return: None
    """
    bot.add_cog(MiscellaneousCog(bot))
