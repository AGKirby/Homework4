import unittest
import q1_cube

class testCaseAdd(unittest.TestCase):
    def test_volume1(self): #check that the function works
        result = q1_cube.volume(10)
        self.assertEqual(result, 1000)

    def test_volume2(self): #check that it works with floats
        result = q1_cube.volume(3.14)
        self.assertAlmostEqual(result, 30.959144) #almost equal due to minor rounding errors

    def test_volume3(self): #check that it returns an error with type errors
        result = q1_cube.volume("Hello World")
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()