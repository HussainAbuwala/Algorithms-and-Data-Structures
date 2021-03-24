import unittest
from hash_table_task5 import SeperateChaining

class test_Task5(unittest.TestCase):

    def test_init_(self):
        self.assertRaises(AssertionError, SeperateChaining, -1)

    def test_setitem(self):
        dict = SeperateChaining(2)
        dict['HELLO'] = 'mama'

        self.assertEqual(dict.__setitem__('MAMA','KHELA'),None)

    def test_getitem_(self):
        dict = SeperateChaining(2)
        dict['HELLO'] = 'mama'
        self.assertEqual(dict.__getitem__('HELLO'),'mama')
        self.assertRaises(KeyError,dict.__getitem__,'SUDANI')

    def test_contains_(self):
        dict = SeperateChaining(2)
        dict['HELLO'] = 'mama'
        self.assertTrue('HELLO' in dict)
        self.assertFalse('S' in dict)

    def test_hash(self):
        dict = SeperateChaining()
        try:
            dict.hash('SODA')
            dict.hash('KALU')
            dict.hash(1)
        except AssertionError:
            pass






