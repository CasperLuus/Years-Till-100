import unittest
from till100 import *

class TestTill100(unittest.TestCase):

    def test_verify_name(self):
        self.assertTrue(verify_name("T"))           #1 letter name              | should PASS |
        self.assertTrue(verify_name("John"))        #name                       | should PASS |
        self.assertTrue(verify_name("Pete Blue"))   #full name                  | should PASS |
        self.assertFalse(verify_name(""))           #empty input                | should FAIL |
        self.assertFalse(verify_name("      "))     #extended empty input       | should FAIL |

    def test_verify_age(self):
        self.assertTrue(verify_age("5"))            #single digit number        | should PASS |
        self.assertTrue(verify_age("20"))           #double digit number        | should PASS |
        self.assertTrue(verify_age("105"))          #higher than 100            | should PASS |
        self.assertFalse(verify_age("John"))        #string                     | should FAIL |
        self.assertFalse(verify_age("ij78fsd"))     #combination string and int | should FAIL |
        self.assertFalse(verify_age("0"))           #0                          | should FAIL |
        self.assertFalse(verify_age("-20"))         #lower than 0               | should FAIL |
        self.assertFalse(verify_age(""))            #empty input                | should FAIL |
        self.assertFalse(verify_age("       "))     #extended empty input       | should FAIL |

    def test_calculate_years_till_100(self):
        self.assertEqual(calculate_years_till_100(20), 80)
        self.assertEqual(calculate_years_till_100(75), 25)
        self.assertEqual(calculate_years_till_100(36), 64)

    def test_results(self):
        self.assertEqual(age_results("John", 100-34),   #The typical expected result
        "You will turn 100 in 66 years. Hope you enjoy these precious years of your life John!")
        self.assertEqual(age_results("Penny", 100-155), #Over the age of 100
        "WOW! You've really lived a long time. Guess I gotta make a new calculator just for you Penny. What your next milestone?")
        self.assertEqual(age_results("Sam", 0),         #Exactly 100
        "You're' already 100! Congrats on the long life Sam.")


if __name__ == '__main__':
    unittest.main()