"""Unit test for reading CSV data back in"""

import csv
import os
import unittest
from fit_and_plot import read_data_from_csv

def create_test_csv(file_path):
    """Creates a temporary CSV file for testing."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['x', 'y', 'sigma'])
        writer.writeheader()
        writer.writerow({'x': '1.0', 'y': '2.0', 'sigma': '0.1'})
        writer.writerow({'x': '2.0', 'y': '4.0', 'sigma': '0.2'})
        writer.writerow({'x': '3.0', 'y': '6.0', 'sigma': '0.3'})

def test_read_data_from_csv():
    """Tests the read_data_from_csv function."""
    test_csv_path = 'test_grouped_data_filtered.csv'
    create_test_csv(test_csv_path)

    try:
        result = read_data_from_csv(test_csv_path)

        # Expected output
        expected_result = {
            'distances': [1.0, 2.0, 3.0],
            'velocities': [2.0, 4.0, 6.0],
            'sigmas': [0.1, 0.2, 0.3]
        }

        # Check if the result matches the expected output
        unittest.TestCase().assertEqual(result, expected_result)
        print("test_read_data_from_csv passed.")
    finally:
        # Clean up the temporary CSV file
        os.remove(test_csv_path)

test_read_data_from_csv()
