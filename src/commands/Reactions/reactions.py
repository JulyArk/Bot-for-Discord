import pickle
import discord


class BotReaction:
    """
    Bot reacts to a keyword/s
    """

    def __init__(self, path):
        """
        :param path: file name or true path, place to save the dictionary as a pickle
        """
        self.file_path = path
        self.keywords = self.load_dict_from_file()
        if self.keywords is None:
            self.keywords = {}

    def save_dict_to_file(self):
        """
        Saves the dictionary updates
        :return: None
        """
        file = open(self.file_path, "wb")
        pickle.dump(self.keywords, file)
        file.close()

    def load_dict_from_file(self):
        """
        Loads the dictionary
        :return: None
        """
        try:
            file = open(self.file_path, "rb")
            dict_holder = pickle.load(file)
            file.close()
            return dict_holder
        except EOFError:
            self.keywords = {}
        except FileNotFoundError:
            file = open(self.file_path, "wb")
            file.close()

    def add_reaction(self, message: str):
        """
        Adds a reaction in the dict for the keyword/s
        :param message: message.contents from discord.py or the literal string of the discord message
        :return: status of the action, -1 on invalid input, 0 on already present, 1 on success
        """
        try:
            contents = message.split()
            contents.pop(0)
            emoji_id = int(''.join(filter(str.isdigit, contents[len(contents) - 1])))
            contents.pop(len(contents) - 1)
            key = " ".join(contents)
            if key in self.keywords:
                return 0
            else:
                self.keywords[key] = emoji_id
                return [key, emoji_id]
        except Exception:
            return -1

    def remove_reaction(self, key: str):
        """
        Removes a reaction from dict
        :param key:
        :return: status of the action, -1 on invalid input, 0 on already present, 1 on success
        """
        if key is None:
            return 0
        elif key not in self.keywords:
            return -1
        self.keywords.pop(key)
        return 1

    def import_guild_reactions(self, filename):
        file = open(filename, "rb")
        dict_holder = pickle.load(file)
        self.keywords = dict_holder
        self.save_dict_to_file()
