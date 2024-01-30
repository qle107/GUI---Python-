import unittest
import src.Controller.util as util


class UnitTestForUtil(unittest.TestCase):
    def test_calculate_percentage(self):
        correct_input = [True, False, True]
        expected_res = 0.66
        test_res = util.calculate_percentage(correct_input)
        self.assertAlmostEqual(expected_res, test_res)  # add assertion here

    def test_calculate_percentage_fail(self):
        wrong_input = [False, False, True, 0.2]
        self.assertTrue(isinstance(util.calculate_percentage(wrong_input), ValueError))

    def test_calculate_percentage_null(self):
        self.assertFalse(isinstance(util.calculate_percentage([]), Exception))
        self.assertIsNone(util.calculate_percentage([]))


if __name__ == '__main__':
    unittest.main()
