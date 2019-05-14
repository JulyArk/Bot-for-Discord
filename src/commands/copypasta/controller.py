from src.commands.copypasta.copypastas import CopyPastas
from classified.globals import copypasta_file_path


class CopyPastaController:
    """
    A controller for the CopyPasta Class
    """

    def __init__(self):
        """
        Loads the file
        """
        self.pastas = CopyPastas(copypasta_file_path)

    def add(self, string: str):
        """
        Add a copy pasta
        :param string: message.context from Discord.py
        :return:
        """
        status = self.pastas.add_pasta(string)
        if status == 0:
            return 0
        elif status == -1:
            return -1
        self.pastas.save_dict_to_file()

    def get(self, key: str):
        """
        Returns a copy pasta / message for key
        :param key: a string/ key / message that triggers a keyword
        :return: string, a copypasta
        """
        return self.pastas.pasta_dict[key]

    def remove(self, key):
        """
        Removes a copypasta
        :param key: key of the copypasta to be removed
        :return: status = if the copy pasta was found and removed or not
        """
        status = self.pastas.remove_pasta(key)
        self.pastas.save_dict_to_file()
        return status

    def get_dict(self):
        """
        Returns the dictionary of copypastas
        :return: dictionary
        """
        return self.pastas.pasta_dict
