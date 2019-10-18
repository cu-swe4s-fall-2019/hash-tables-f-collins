import unittest
import random
import hash_functions as hf


class TestHashFunctions(unittest.TestCase):
    def test_h_ascii_single_char(self):
        randval = random.randint(32, 126) # get random printable ASCII char
        randn = random.randint(1, 100)
        self.assertEqual(randval % randn, hf.h_ascii(str(chr(randval)), randn))

    def test_h_ascii_random_str(self):
        for test in range(0, 1000):
            randstr = ""
            randlen = random.randint(1, 20)
            randn = random.randint(1, 100)
            strsum = 0;
            for i in range(randlen):
                randchar = random.randint(32, 126)
                randstr += chr(randchar)
                strsum += randchar
            
            self.assertEqual(strsum % randn, hf.h_ascii(randstr, randn))

    def test_h_ascii_empty_str(self):
        self.assertEqual(0, hf.h_ascii("", random.randint(1,100))) 

    def test_h_ascii_invalid_n(self):
        self.assertEqual(None, hf.h_ascii("whatever", random.randint(-100,0)))

    def test_h_ascii_non_string_key(self):
        randnum = random.randint(0,1000)
        randn = random.randint(0,100) 
        strsum = 0
        for char in str(randnum):
            strsum += ord(char)

        self.assertEqual(strsum % randn, hf.h_ascii(randnum, randn))

    def test_h_rolling_single_char(self):
        randval = random.randint(32, 126)
        randn = random.randint(1, 100)

        s = randval % 2 ** 64

        self.assertEqual(s % randn, hf.h_rolling(str(chr(randval)), randn))

    def test_h_rolling_random_str(self):
        for test in range(0, 1000):
            randstr = ""
            randlen = random.randint(1, 20)
            randn = random.randint(1, 100)
            s = 0
            for i in range(randlen):
                randchar = random.randint(32, 126)
                randstr += chr(randchar)
                s += randchar * 53 ** i

            s = s % 2 ** 64

            self.assertEqual(s % randn, hf.h_rolling(randstr, randn))

    def test_h_rolling_empty_str(self):
        self.assertEqual(0, hf.h_rolling("", random.randint(1,100))) 

    def test_h_rolling_invalid_n(self):
        self.assertEqual(None, hf.h_rolling("whatever", random.randint(-100,0)))

    def test_h_rolling_non_string_key(self):
        randnum = random.randint(0,1000)
        randn = random.randint(1,100) 
        randstr = str(randnum)

        self.assertEqual(hf.h_rolling(str(randnum), randn), hf.h_rolling(randnum, randn))



if __name__ == "__main__":
    unittest.main()
