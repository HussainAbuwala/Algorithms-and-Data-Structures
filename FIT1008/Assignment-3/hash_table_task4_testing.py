import unittest
from hash_table_task4 import QuadraticProbeTable

class test_Task4(unittest.TestCase):

    def test_init_(self):
        self.assertRaises(AssertionError, QuadraticProbeTable, -1)

    def test_setitem(self):
        dict = QuadraticProbeTable(6)
        dict['HELLO'] = 'mama'

        self.assertEqual(dict.__setitem__('MAMA','KHELA'),None)
        dict = QuadraticProbeTable(2)
        dict['HELLO'] = 'mama'
        self.assertRaises(IndexError,dict.__setitem__,'SODA','KALA')

    def test_getitem_(self):
        dict = QuadraticProbeTable(2)
        dict['HELLO'] = 'mama'
        self.assertEqual(dict.__getitem__('HELLO'),'mama')
        self.assertRaises(KeyError,dict.__getitem__,'SUDANI')

    def test_contains_(self):
        dict = QuadraticProbeTable(2)
        dict['HELLO'] = 'mama'
        self.assertTrue('HELLO' in dict)
        self.assertFalse('S' in dict)

    def test_hash(self):
        dict = QuadraticProbeTable()
        try:
            dict.hash('SODA')
            dict.hash('KALU')
            dict.hash(1)
        except AssertionError:
            pass

    def test_len_(self):
        dict = QuadraticProbeTable(5)
        self.assertEqual(len(dict),0)
        dict['HELLO'] = 'SODA'
        dict['MAMA'] = 'KHELA'
        self.assertEqual(len(dict), 2)




