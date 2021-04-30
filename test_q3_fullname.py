import unittest
import q3_fullname

class testCaseAdd(unittest.TestCase):
    def test_fullname1(self): #check that the function works as intended
        result = q3_fullname.fullname("Adam", "Graneto")
        self.assertEqual(result, "Adam Graneto")

    def test_fullname2(self): #check that the function works as intended
        result = q3_fullname.fullname(1, 2)
        self.assertEqual(result, None)

    def test_fullname3(self): #check that the function works as intended
        result = q3_fullname.fullname(["Hello"], ["World"])
        self.assertEqual(result, "Hello World")

if __name__ == "__main__":
    unittest.main()