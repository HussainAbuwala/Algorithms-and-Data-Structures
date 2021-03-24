import unittest
from Task1 import List


class test_Task1(unittest.TestCase):

    def test_init_(self):
        self.assertRaises(AssertionError,List,-1)
        self.assertRaises(AssertionError,List,(1,2,3))
        self.assertRaises(AssertionError,List,101)

    def test_str_(self):
        my_list = List(5)
        self.assertEqual(str(my_list),'""')
        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        self.assertEqual(str(my_list),'"1\n 2\n 3"' )

    def test_len_(self):
        my_list = List(5)
        self.assertEqual(len(my_list),0)
        my_list.append(1)
        my_list.append(2)
        self.assertEqual(len(my_list), 2)

    def test_contains_(self):
        my_list = List(5)
        self.assertFalse(2 in my_list)
        my_list.append(0)
        my_list.append([])
        self.assertTrue([] in my_list)

    def test_getitem_(self):
        my_list = List(4)
        self.assertRaises(AssertionError,my_list.__getitem__,(1,2,3))
        self.assertRaises(IndexError,my_list.__getitem__,-1)
        self.assertRaises(IndexError,my_list.__getitem__,0)
        my_list.append(1)
        my_list.append(2)
        self.assertEqual(my_list[0],1)

    def test_setitem(self):
        my_list = List(5)
        self.assertRaises(AssertionError,my_list.__setitem__,[],2)
        self.assertRaises(IndexError,my_list.__setitem__,-1,2)
        self.assertRaises(IndexError,my_list.__setitem__,0,2)
        my_list.append(1)
        my_list.append(2)
        self.assertTrue(my_list.__setitem__(0,5))

    def test_eq_(self):
        my_list = List(4)
        self.assertRaises(AssertionError, my_list.__eq__, (1, 2, 3))
        self.assertFalse([1,2,3] == my_list)
        my_list.append(1)
        my_list.append(2)
        self.assertTrue([1,2] == my_list)
        alist = List(2)
        alist.append(1)
        alist.append(2)
        self.assertTrue(alist == my_list)


    def test_is_empty(self):
        my_list = List(4)
        self.assertTrue(my_list.is_empty())
        my_list.append(1)
        my_list.append(2)
        self.assertFalse(my_list.is_empty())

    def test_is_full(self):
        my_list = List(2)
        self.assertFalse(my_list.is_full())
        my_list.append(1)
        my_list.append(2)
        self.assertTrue(my_list.is_full())

    def test_append(self):
        my_list = List(2)
        self.assertTrue(my_list.append(1))
        my_list.append(2)
        self.assertFalse(my_list.append(5))

    def test_insert(self):
        my_list = List(2)
        self.assertRaises(AssertionError, my_list.insert, [], 2)
        self.assertRaises(IndexError, my_list.insert, -1, 2)
        my_list.append(1)
        self.assertTrue(my_list.insert(0,3))

    def test_remove(self):
        my_list = List(3)
        self.assertRaises(AssertionError,my_list.remove,1)
        my_list.append(1)
        my_list.append(2)
        self.assertRaises(ValueError,my_list.remove,3)
        self.assertTrue(my_list.remove(1))

    def test_delete(self):
        my_list = List(3)
        self.assertRaises(AssertionError, my_list.delete, [])
        self.assertRaises(IndexError, my_list.delete, -1)
        self.assertRaises(IndexError, my_list.delete, 0)
        my_list.append(1)
        my_list.append(2)
        self.assertTrue(my_list.delete(0))



if __name__ == '__main__':
    unittest.main()