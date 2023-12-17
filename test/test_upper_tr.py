import unittest

from turkish_string import upper_tr


class TestUpperTr(unittest.TestCase):
    def test_upper_tr(self):
        """
        Tests for upper_tr
        """
        self.assertEqual(upper_tr(''), '')
        self.assertEqual(upper_tr(' '), ' ')
        self.assertEqual(upper_tr('kadıköy'), 'KADIKÖY')
        self.assertEqual(upper_tr('istanbul'), 'İSTANBUL')
        self.assertEqual(upper_tr(' istanbul kadıköy '), ' İSTANBUL KADIKÖY ')
        self.assertRaises(TypeError, upper_tr, 3)


if __name__ == '__main__':
    unittest.main()