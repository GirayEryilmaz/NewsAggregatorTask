import unittest

from public_apis.api_config import registry
import importlib


class TestNewsApi(unittest.TestCase):

    def test_list_functions(self):
        for module_name, class_name in registry:
            module = importlib.import_module('public_apis.'+module_name)
            my_class = getattr(module, class_name)
            news = my_class.list_news()
            self.assertIsInstance(news, list)
            self.assertGreater(len(news), 0)

if __name__ == '__main__':
    unittest.main()
