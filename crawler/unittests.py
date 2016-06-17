import unittest
from rank import Rank

# data for parse - url, persons
page = '''<html>
            <body>
                <p>Путин тут</p>
                <a>Путин молодец ли. Путину так все ппц. Что Путиным?</a>
                <p>Медведев тут</p>
                <a>Медведев молодцомм а? Медведевым сделано. Что дали Медведеву?</a>
            </body>
        </html>'''

empty_page = ''

words_dict = {1: ['Путин', 'путину', 'путиным'],
              2: ['Медведев', 'Медведевым', 'медведеву']}
word = 'Путин'


# parse url
class TestParseUrl(unittest.TestCase):

    rank = Rank()

    def test_CountRankPersonInPage(self):
        self.assertEqual(self.rank.counts_in(
            page, words_dict), {1: 4, 2: 4})

    def test_CountRankPersonInEmptyPage(self):
        self.assertEqual(self.rank.counts_in(
            empty_page, words_dict), {1: 0, 2: 0})

    # def test_SaveRank(self):
    #     data = self.rank.counts_in(page, words_dict)
    #     self.assertEqual(self.rank.save(data))


if __name__ == '__main__':
    unittest.main()
