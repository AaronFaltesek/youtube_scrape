import unittest

from .hello import hello1
from youtube_scrape import __main__

class TestMain(unittest.TestCase):

    def test_main_test(self):
        #self.assertEqual(hello1(), True)
        self.assertEqual(__main__.test_main(), True)

    def test_main(self):
        #self.assertEqual(hello1(), True)
        self.assertEqual(__main__.test_main(), True)


    # def test_test_main(self):
    #     x = __main__.test_main()
    #     self.assertEqual(x, True)

if __name__ == '__main__':
    unittest.main()