from app import PoeItemCrawler
import unittest
from unittest.mock import MagicMock

class PoeItemCrawlerTest(unittest.TestCase):
    def test_average_of_list(self):
        poe = PoeItemCrawler('x')
        result = poe.average_of_list([1, 2, 3])
        self.assertEqual(result, 2)
    
    def test_item_reader(self):
        poe = PoeItemCrawler('23')
        list_of_items = poe.item_reader()
        self.assertEqual(list_of_items, [1, 71, 73])


