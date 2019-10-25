import unittest
import random
import hash_tables as ht


class TestHashTables(unittest.TestCase):
    def test_linearprobe_h_ascii_single_element(self):
        table = ht.LinearProbe(1, ht.h_ascii)
        randstr = ""
        strlen = random.randint(1,50)
        randval = random.randint(0,999)

        for char in range(0, strlen):
            randstr += chr(random.randint(32, 126))

        table.add(randstr, randval)

        self.assertEqual(randval, table.search(randstr))


if __name__ == "__main__":
    unittest.main()
