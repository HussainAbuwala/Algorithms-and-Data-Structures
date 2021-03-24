import unittest
from task7_cmd_class_testing import Special_Command_Line
from task7_cmd_class_testing import List

class test_Task7(unittest.TestCase):

    def test_read_file(self):
        text_ed = Special_Command_Line()
        self.assertFalse(text_ed.read_file(123))
        self.assertTrue(text_ed.read_file('antibiot.txt'))


    def test_write_file(self):
        text_ed = Special_Command_Line()
        self.assertEqual(text_ed.Write_Filename(123),(False,None))
        self.assertTrue(text_ed.read_file('sonu.txt'))
        self.assertEqual(text_ed.Write_Filename('tasin_aryan11.txt'),('Old File Re-written',['hello']))


    def test_print_num(self):
        text_ed = Special_Command_Line()
        self.assertFalse(text_ed.PrintNum(-1))
        self.assertTrue(text_ed.read_file('CD_Store.txt'))
        self.assertTrue(text_ed.PrintNum(''))

    def test_frequency(self):
        text_ed = Special_Command_Line()
        self.assertFalse(text_ed.frequency())
        self.assertTrue(text_ed.read_file('CD_Store.txt'))
        self.assertTrue(text_ed.frequency())