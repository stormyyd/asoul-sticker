import unittest
import json
import os

class TestData(unittest.TestCase):

    def test_data(self):
        with open('data.txt', encoding='utf8') as f:
            for line in [l.strip() for l in f]:
                if len(line) == 0 or line[0] == '#':
                    continue
                columns = line.split(' ')
                self.assertEqual(len(columns), 4)
                self.assertTrue(os.path.isfile(os.path.join('./asset', columns[0], columns[1])))

    def test_config(self):
        with open('config.json', encoding='utf8') as f:
            config = json.load(f)
        self.assertIsNotNone(config)
        self.assertIsNotNone(config['host'])
        self.assertIsNotNone(config['height'])
