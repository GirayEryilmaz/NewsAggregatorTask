import unittest

from public_apis.reddit import RedditHandler

class TestRedditApi(unittest.TestCase):

    def test_get_news_list(self):
        reslist = RedditHandler.list_news()
        self.assertIsInstance(reslist, list)
        self.assertGreater(len(reslist), 0)

    def test_search(self):
        reslist = RedditHandler.search('corona')
        self.assertIsInstance(reslist, list)
        self.assertGreater(len(reslist), 0)


if __name__ == '__main__':
    unittest.main()
