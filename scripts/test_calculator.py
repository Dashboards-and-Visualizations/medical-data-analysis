import unittest
import pandas as pd
import numpy as np
from calculator import load_data, process_data, convert_to_long_format, plot_category_data, clean_data, plot_correlation_matrix

class TestMedicalDataVisualizer(unittest.TestCase):

    def setUp(self):
        # Create a sample dataframe for testing
        data = {
            'id': [0, 1, 2, 3, 4],
            'age': [50, 55, 60, 45, 65],
            'sex': [1, 2, 1, 2, 1],
            'height': [165, 160, 175, 170, 180],
            'weight': [70, 60, 80, 75, 85],
            'ap_hi': [120, 130, 140, 125, 135],
            'ap_lo': [80, 85, 90, 82, 88],
            'cholesterol': [1, 2, 1, 2, 3],
            'gluc': [1, 1, 2, 2, 3],
            'smoke': [0, 1, 0, 0, 1],
            'alco': [0, 0, 1, 1, 0],
            'active': [1, 0, 1, 1, 0],
            'cardio': [0, 1, 0, 1, 1]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        # Test loading data from a valid file path
        try:
            df = load_data('../data/medical_examination.csv')
            self.assertIsInstance(df, pd.DataFrame)
        except Exception as e:
            self.fail(f"load_data raised an exception: {e}")

        # Test loading data from an invalid file path
        with self.assertRaises(FileNotFoundError):
            load_data('invalid/path/to/file.csv')

    def test_process_data(self):
        # Test the process_data function
        df_processed = process_data(self.df.copy())
        self.assertIn('overweight', df_processed.columns)
        self.assertIn('cholesterol', df_processed.columns)
        self.assertIn('gluc', df_processed.columns)
        self.assertEqual(df_processed['overweight'].dtype, np.int32)

    def test_convert_to_long_format(self):
        # Add 'overweight' column to the test DataFrame
        self.df['height'] = self.df['height'] / 100
        self.df['bmi'] = self.df['weight'] / (self.df['height'] ** 2)
        self.df['overweight'] = np.where(self.df['bmi'] > 25, 1, 0)

        df_long = convert_to_long_format(self.df.copy())
        self.assertIn('variable', df_long.columns)
        self.assertIn('value', df_long.columns)
        self.assertIn('cardio', df_long.columns)

    def test_plot_category_data(self):
        # Add 'overweight' column to the test DataFrame
        self.df['height'] = self.df['height'] / 100
        self.df['bmi'] = self.df['weight'] / (self.df['height'] ** 2)
        self.df['overweight'] = np.where(self.df['bmi'] > 25, 1, 0)

        df_long = convert_to_long_format(self.df.copy())

        try:
            plot_category_data(df_long, '../figures/category-plot-test.jpg')
        except Exception as e:
            self.fail(f"plot_category_data raised an exception: {e}")

    def test_clean_data(self):
        # Test the clean_data function
        df_cleaned = clean_data(self.df.copy())
        self.assertGreaterEqual(len(self.df), len(df_cleaned))

    def test_plot_correlation_matrix(self):
        # Test the plot_correlation_matrix function
        try:
            plot_correlation_matrix(self.df.copy(), '../figures/medical-data-test.jpg')
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
