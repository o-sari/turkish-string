import unittest

from turkish_string import capitalize_tr


class TestCapitalizeTr(unittest.TestCase):
    def test_capitalize_tr(self):
        """
        Tests for capitalize_tr
        """
        self.assertEqual(capitalize_tr(''), '')
        self.assertEqual(capitalize_tr(' '), ' ')
        self.assertEqual(capitalize_tr('iI'), 'İı')
        self.assertEqual(capitalize_tr('KIRIK'), 'Kırık')
        self.assertEqual(capitalize_tr('İSTANBUL'), 'İstanbul')
        self.assertEqual(capitalize_tr('istanbul'), 'İstanbul')
        self.assertEqual(capitalize_tr('İSTANBUL KADIKÖY'), 'İstanbul kadıköy')
        self.assertEqual(capitalize_tr(' İSTANBUL KADIKÖY '), ' istanbul kadıköy ')
        self.assertRaises(TypeError, capitalize_tr, 3)


if __name__ == '__main__':
    unittest.main()