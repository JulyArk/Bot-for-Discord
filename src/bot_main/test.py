class abcd:
    pasta_dict = {}
    def add_blacklist(self, blacklist: str, channel, blklistType: str):
        """
        TODO
        """
        if channel in self.pasta_dict:
            if blklistType in self.pasta_dict[channel]:
                if blacklist in self.pasta_dict[channel][blklistType]:
                    return -1  # already exists
                else:
                    self.pasta_dict[channel][blklistType].append(blacklist)
            else:
                self.pasta_dict[channel][blklistType] = []
                self.pasta_dict[channel][blklistType].append(blacklist)
        else:
            self.pasta_dict[channel] = {}  # Add it to dictionary
            self.pasta_dict[channel][blklistType] = []
            self.pasta_dict[channel][blklistType].append(blacklist)

    def test(self, data):
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


x = abcd()
print(x.test("abcd 3343464 but 11111 222 3333333 77777 444"))