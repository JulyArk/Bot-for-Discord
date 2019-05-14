import pickle


class CopyPastas:
    """
    A Class meant to store bot replies to certain words/ sentences
    Eg:
    -User types: "abc"
    -Bot responds with: "def"
    """

    def __init__(self, path):
        """
        A file path where to store the dictionary of copypastas in a pickle format
        :param path: file name or true path
        """
        self.file_path = path
        self.pasta_dict = self.load_dict_from_file()
        if self.pasta_dict is None:
            self.pasta_dict = {}

    @staticmethod
    def get_the_pasta(string: str):
        """

        :param string: receives a message.context (a string) and formats the contents ass a pasta
        :return: keymark (key) to be added in dictionary containing pasta (message)
        """
        try:

            keymark = string.split()
            keymark.pop(0)
            keymark = " ".join(keymark).split('"')[0]
            keymark = keymark[:-1]
            pasta = string.split('"')[1]
        except IndexError:
            keymark = None
            pasta = None
        return keymark, pasta

    def save_dict_to_file(self):
        """
        Saves the dictionary to the file
        """
        file = open(self.file_path, "wb")
        pickle.dump(self.pasta_dict, file)
        file.close()

    def load_dict_from_file(self):
        """
        Loads the dictionary from the file
        """
        try:
            file = open(self.file_path, "rb")
            dict_holder = pickle.load(file)
            file.close()
            return dict_holder
        except EOFError:
            self.pasta_dict = {}
        except FileNotFoundError:
            file = open(self.file_path, "wb")
            file.close()

    def add_pasta(self, string: str):
        """
        Adds a copypasta
        :param string: message.or the full discord message from the user
        :return: status of the action -1 for invalid input, 0 for already present and 1 for success
        """
        key, pasta = self.get_the_pasta(string)
        if key is None:
            return -1
        elif key in self.pasta_dict:
            return 0
        if not self.test_pasta_text(pasta):
            return -1
        self.pasta_dict[key] = pasta
        return 1

    def remove_pasta(self, key: str):
        """
        Removes a copypasta
        :param key: the key of the message
        :return: status of the action, 0 for invalid input, -1 for not found, 1 for success
        """
        key = key.split()
        key.pop(0)
        key = " ".join(key)
        print(key)

        if key is None:
            return 0
        elif key not in self.pasta_dict:
            return -1
        self.pasta_dict.pop(key)
        return 1

    @staticmethod
    def test_pasta_text(pasta):
        """
        Checks if the message contents are good
        :param pasta: the message that gets sent by typing a key
        :return: True or False
        """
        print(len(pasta))
        if len(pasta) > 200:
            return False
        elif len(pasta) < 3:
            return False
        return True
