import unittest

from turkish_string import title_tr


class TestTitleTr(unittest.TestCase):
    def test_title_tr(self):
        """
        Tests for title_tr
        """
        self.assertEqual(title_tr(''), '')
        self.assertEqual(title_tr(' '), ' ')
        self.assertEqual(title_tr('iI ıİ'), 'İı Ii')
        self.assertEqual(title_tr('KADIKÖY'), 'Kadıköy')
        self.assertEqual(title_tr('İSTANBUL'), 'İstanbul')
        self.assertEqual(title_tr('istanbul'), 'İstanbul')
        self.assertEqual(title_tr('İSTANBUL KADIKÖY'), 'İstanbul Kadıköy')
        self.assertEqual(title_tr(' İSTANBUL KADIKÖY '), ' İstanbul Kadıköy ')
        self.assertRaises(TypeError, title_tr, 3)


if __name__ == '__main__':
    unittest.main()