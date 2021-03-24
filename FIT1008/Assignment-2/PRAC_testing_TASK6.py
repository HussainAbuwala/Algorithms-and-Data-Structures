import unittest
from task6_cmd_class_testing import Command_Line
from task6_cmd_class_testing import List

class test_Task6(unittest.TestCase):
    def test_read_file(self):
        text_ed = Command_Line()
        self.assertFalse(text_ed.read_file(123))
        self.assertTrue(text_ed.read_file('antibiot.txt'))

    def test_write_file(self):
        text_ed = Command_Line()
        self.assertFalse(text_ed.Write_Filename(123))
        self.assertTrue(text_ed.read_file('CD_Store.txt'))
        self.assertTrue(text_ed.Write_Filename('1234.txt'))

    def test_print_num(self):
        text_ed = Command_Line()
        self.assertFalse(text_ed.PrintNum(-1))
        self.assertTrue(text_ed.read_file('CD_Store.txt'))
        self.assertTrue(text_ed.PrintNum(''))

    def test_frequency(self):
        text_ed = Command_Line()
        self.assertFalse(text_ed.frequency())
        self.assertTrue(text_ed.read_file('CD_Store.txt'))
        self.assertTrue(text_ed.frequency())
