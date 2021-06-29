import unittest
from Calculator import Calculator
from csvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Addition.csv").get_data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Subtraction.csv").get_data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Multiplication.csv").get_data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Division.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Square.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_squareroot_method_calculator(self):
        test_data = CsvReader("/src/data/Unit Test Square Root.csv").get_data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square_root(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def tearDown(self) -> None:
        # self.calculator.dispose()
        pass

if __name__ == "__main__":
    unittest.main()