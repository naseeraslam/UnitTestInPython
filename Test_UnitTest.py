import unittest

from BasicMath import BasicMath


class LearnTestClass(unittest.TestCase):
    def setUp(self) -> None:
        print("Setup is called")
        self.bm = BasicMath()

    def tearDown(self) -> None:
        super().tearDown()
        print("Tear Down Called......")

    def test_Add(self):
        result = self.bm.add(self.bm.a, self.bm.b)
        self.assertEqual(result, 10, msg="Test is not passed")

    def test_Mul(self):
        result = self.bm.multiply(self.bm.a, self.bm.b)
        self.assertEqual(result, 25, msg="Test is not passed")
        self.assertIsNot(self.bm.a, self.bm.b)

    def test_name(self):
        result = self.bm.name('')
        self.assertIsNone(result, msg="Name is not none")
        self.assertTrue(self.bm.a == self.bm.b)

    def test_divide(self):
        self.assertRaises(Exception, self.bm.divide, (self.bm.a,  0))


if __name__ == '__main__':
    unittest.main()
