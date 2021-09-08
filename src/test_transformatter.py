import datetime
import unittest
import transformatter

class TransformatterTest(unittest.TestCase):
    def test_string_to_date(self):
        date_string = transformatter.string_to_date('2021-09-07 00:00:00')
        self.assertEqual(datetime.datetime(2021, 9, 7, 0, 0, 0), date_string)

if __name__ == '__main__':
    unittest.main()