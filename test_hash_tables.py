import unittest
import random
import hash_tables as ht


class TestHashTables(unittest.TestCase):
    def test_linearprobe_h_ascii_single_element(self):
        table = ht.LinearProbe(1, ht.h_ascii)
        randstr = ""
        strlen = random.randint(1, 50)
        randval = random.randint(0, 999)

        for char in range(0, strlen):
            randstr += chr(random.randint(32, 126))

        table.add(randstr, randval)

        self.assertEqual(randval, table.search(randstr))

    def test_linearprobe_h_ascii_multiple_elements(self):
        tablesize = 1000
        table = ht.LinearProbe(tablesize, ht.h_ascii)
        tabledict = {}

        for i in range(0, 500):
            randkey = ""
            randomval = random.randint(0, 100)
            for i in range(0, random.randint(1, 50)):
                randkey += chr(random.randint(32, 126))
            if randkey in tabledict:
                continue
            else:
                if table.add(randkey, randomval) == -1:
                    break
                else:
                    tabledict[randkey] = randomval
                    table.add(randkey, randomval)

        for key in tabledict:
            self.assertEqual(tabledict[key], table.search(key))

    def test_linearprobe_h_rolling_single_element(self):
        table = ht.LinearProbe(1, ht.h_rolling)
        randstr = ""
        strlen = random.randint(1, 50)
        randval = random.randint(0, 999)

        for char in range(0, strlen):
            randstr += chr(random.randint(32, 126))

        table.add(randstr, randval)

        self.assertEqual(randval, table.search(randstr))

    def test_linearprobe_h_rolling_multiple_elements(self):
        tablesize = 1000
        table = ht.LinearProbe(tablesize, ht.h_rolling)
        tabledict = {}

        for i in range(0, 500):
            randkey = ""
            randomval = random.randint(0, 100)
            for i in range(0, random.randint(1, 50)):
                randkey += chr(random.randint(32, 126))
            if randkey in tabledict:
                continue
            else:
                if table.add(randkey, randomval) == -1:
                    break
                else:
                    tabledict[randkey] = randomval
                    table.add(randkey, randomval)

        for key in tabledict:
            self.assertEqual(tabledict[key], table.search(key))

    def test_chainedhash_h_ascii_single_element(self):
        table = ht.ChainedHash(1, ht.h_ascii)
        randstr = ""
        strlen = random.randint(1, 50)
        randval = random.randint(0, 999)

        for char in range(0, strlen):
            randstr += chr(random.randint(32, 126))

        table.add(randstr, randval)

        self.assertEqual(randval, table.search(randstr))

    def test_chainedhash_h_ascii_multiple_elements(self):
        tablesize = 1000
        table = ht.ChainedHash(tablesize, ht.h_ascii)
        tabledict = {}

        for i in range(0, 500):
            randkey = ""
            randomval = random.randint(0, 100)
            for i in range(0, random.randint(1, 50)):
                randkey += chr(random.randint(32, 126))
            if randkey in tabledict:
                continue
            else:
                if table.add(randkey, randomval) == -1:
                    break
                else:
                    tabledict[randkey] = randomval
                    table.add(randkey, randomval)

        for key in tabledict:
            self.assertEqual(tabledict[key], table.search(key))

    def test_chainedhash_h_rolling_single_element(self):
        table = ht.ChainedHash(1, ht.h_rolling)
        randstr = ""
        strlen = random.randint(1, 50)
        randval = random.randint(0, 999)

        for char in range(0, strlen):
            randstr += chr(random.randint(32, 126))

        table.add(randstr, randval)

        self.assertEqual(randval, table.search(randstr))

    def test_chainedhash_h_rolling_multiple_elements(self):
        tablesize = 1000
        table = ht.ChainedHash(tablesize, ht.h_rolling)
        tabledict = {}

        for i in range(0, 500):
            randkey = ""
            randomval = random.randint(0, 100)
            for i in range(0, random.randint(1, 50)):
                randkey += chr(random.randint(32, 126))
            if randkey in tabledict:
                continue
            else:
                if table.add(randkey, randomval) == -1:
                    break
                else:
                    tabledict[randkey] = randomval
                    table.add(randkey, randomval)

        for key in tabledict:
            self.assertEqual(tabledict[key], table.search(key))


if __name__ == "__main__":
    unittest.main()
