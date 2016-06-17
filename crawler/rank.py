import re


class Rank:

    @staticmethod
    def __count_in(page, word):
        pattern = re.compile(r'\b{0}\b'.format(word),
                             re.IGNORECASE | re.MULTILINE)
        finded_words = pattern.findall(page)
        return len(finded_words)

    def counts_in(self, page, words_dict):
        ranks = {}
        for _id, words in words_dict.items():
            ranks[_id] = sum(self.__count_in(page, word)
                             for word in words)
        return ranks

    def save_to_mysql(self, rank):
        pass

    def save(self, rank):
        pass
