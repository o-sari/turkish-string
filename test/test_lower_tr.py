import unittest

from turkish_string import lower_tr


class TestLowerTr(unittest.TestCase):
    def test_lower_tr(self):
        """
        Tests for lower_tr
        """
        self.assertEqual(lower_tr(''), '')
        self.assertEqual(lower_tr(' '), ' ')
        self.assertEqual(lower_tr('KADIKÖY'), 'kadıköy')
        self.assertEqual(lower_tr('İSTANBUL'), 'istanbul')
        self.assertEqual(lower_tr(' İSTANBUL KADIKÖY '), ' istanbul kadıköy ')
        self.assertRaises(TypeError, lower_tr, 3)


if __name__ == '__main__':
    unittest.main()