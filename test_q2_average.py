import unittest
import q2_average

class testCaseAdd(unittest.TestCase):
    def test_average1(self): #check that the function works as intended
        result = q2_average.average([1,2,3,4,5])
        self.assertEqual(result, 3)

    def test_average2(self): #check that the function returns None with an empty list
        result = q2_average.average([]) #empty list
        self.assertEqual(result, None)

    def test_average3(self): #check that the function returns None with invalid data types
        result = q2_average.average(["1", "A", "!"])
        self.assertEqual(result, "A")

if __name__ == "__main__":
    unittest.main()