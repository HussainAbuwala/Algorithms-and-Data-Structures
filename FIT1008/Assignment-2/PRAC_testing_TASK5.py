import unittest
from task5_cmd_class_tasting import Command_Line
from task5_cmd_class_tasting import List

class test_Task5(unittest.TestCase):
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





