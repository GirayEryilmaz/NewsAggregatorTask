import unittest

from public_apis.newsapi import NewsApiHandler

class TestNewsApi(unittest.TestCase):

    def test_get_news_list(self):
        reslist = NewsApiHandler.list_news()
        self.assertIsInstance(reslist, list)
        self.assertGreater(len(reslist), 0)
        
    def test_search(self):
        reslist = NewsApiHandler.search('corona')
        self.assertIsInstance(reslist, list)
        self.assertGreater(len(reslist), 0)


if __name__ == '__main__':
    unittest.main()
