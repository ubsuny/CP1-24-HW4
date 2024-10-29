"""
Provides unit testing for linear_fit.py functions.
Tests cases of input errors for the read_data_from_csv function.
Tests several potential errors and also positive results from fit function.

"""
import pytest
import pandas as pd
import linear_fit as linfit

class TestReadCSV:
    """
    Class to test the read_data_from_csv function.
    Tests the following cases:
    - File path and headers not strings: 
    - File not found.
    - Specified headers not in CSV.
    """
    def test_type_error(self):
        """
        Test that function raises expected error for input of invalid type.
        """
        csv = 12345
        with pytest.raises(TypeError, match = "File path and headers must be strings."):
            linfit.read_data_from_csv(csv)

    def test_missing_file(self):
        """
        Test that function raises FileNotFoundError for a missing file.
        """
        csv = 'non_existent_file.csv'
        with pytest.raises(FileNotFoundError, match = "File was not found."):
            linfit.read_data_from_csv(csv)

    def test_header_error(self):
        """
        Tests for expected error with headers not matching specifications.
        """
        # Add sample data to test_placeholder.csv with headers
        data = {
            'Distance (Mpc)': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            'Velocities (km/s)': [-1.0, 1.0, 3.0, 5.0, 7.0, 9.0],
            'Standard Deviation': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        }
        test_csv = 'test_placeholder.csv'
        pd.DataFrame(data).to_csv(test_csv, index=False)

        #Test for expected error.
        with pytest.raises(KeyError, match = "File headers not found in CSV."):
            linfit.read_data_from_csv(test_csv)

        # Reset test_placeholder.csv to blank file.
        pd.DataFrame().to_csv(test_csv, index=False)

class TestFit:
    """
    Contains tests for the fitting function in module.
    Tests the following cases:
     - Positive case CSV (valid data in CSV format).
     - Positive case CSV (valid data in CSV format).
     - Incorrect input type for lists.
     - Incorrect type of elements in lists.
     - Unequal data lengths.
     - Insufficent amount of data for fit.
     - Sigma approaching 0.
     - variance_sum approaching 0.
    """
    def test_positive_csv(self):
        """
        Test the function with a csv file containing mock data with slope of 2
        and intercept of -1. Errors were set to 0.1 arbitrarily.
        Expected values were calculated from equation linear_fit.py is modeled after.
        Placeholder csv is called and then reset by pandas.
        """
        # Add sample data to test_placeholder.csv
        data = {
            'x': [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            'y': [-1.0, 1.0, 3.0, 5.0, 7.0, 9.0],
            'sigma': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        }
        test_csv = 'test_placeholder.csv'
        pd.DataFrame(data).to_csv(test_csv, index=False)

        # Gather data and result:
        x,y,sigma = linfit.read_data_from_csv(test_csv)
        result = linfit.fit(x,y,sigma)

        # Define expected result:
        expected_result = {
            'intercept': -1.0,
            'slope': 2.0,
            'sigma_a': 0.0723747,
            'sigma_b': 0.0239046,
            'chi_squared': 2.95823*10**(-29)
        }

        #Test if data agrees.
        assert expected_result == pytest.approx(result, rel = 1e-5)

        # Reset test_placeholder.csv to blank file.
        pd.DataFrame().to_csv(test_csv, index=False)

    def test_positive_lists(self):
        """
        Test the function with inputs as lists with known outputs.
        Expected values were calculated from equation linear_fit.py is modeled after.
        """
        x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        y = [-1.0, 1.0, 3.0, 5.0, 7.0, 9.0]
        sigma = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        result = linfit.fit(x,y,sigma)

        expected_result = {
            'intercept': -1.0,
            'slope': 2.0,
            'sigma_a': 0.0723747,
            'sigma_b': 0.0239046,
            'chi_squared': 2.95823e-29
        }
        assert result == pytest.approx(expected_result, rel = 1e-5)

    def test_invalid_type(self):
        """
        Tests that function has expected output for invalid input type.
        """
        x = 'string'
        y = [1,2,3]
        sigma = [1,1,1]
        with pytest.raises(TypeError, match="Input not in form of list."):
            linfit.fit(x,y,sigma)

    def test_invalid_element(self):
        """
        Tests that function has expected error for invalid element type.
        """
        x = ['1',2,3]
        y = [1,2,3]
        sigma = [1,1,1]
        with pytest.raises(TypeError, match = "Elements of list are not all numeric."):
            linfit.fit(x,y,sigma)

    def test_unequal_size(self):
        """
        Tests that function has expected error for unequal list sizes.
        """
        x = [1,2,3]
        y = [1,2,3,4]
        sigma = [1,2,3,4,5]
        with pytest.raises(TypeError, match = "Data must be lists of same length."):
            linfit.fit(x,y,sigma)

    def test_insufficient_data(self):
        """
        Tests that function has expected error for len(x) < 2.
        """
        x = [1]
        y = [1]
        sigma = [1]
        with pytest.raises(TypeError, match = "Not enough data to fit."):
            linfit.fit(x,y,sigma)

    def test_sigma_zero(self):
        """
        Tests that function has expected error for a sigma close to 0.
        """
        x = [1,2,3]
        y = [1,2,3]
        sigma = [0.1,0.1,0.0000001]
        # Only tests beginning from long error message
        with pytest.raises(ZeroDivisionError, match = "Element of sigma is too small."):
            linfit.fit(x,y,sigma)

    def test_variance_sum_zero(self):
        """
        Tests that function has expected error for a variance_sum close to 0.
        """
        x = [1,2,3]
        y = [1,2,3]
        sigma = [1e+6,1e+6,1e+6]
        # Only tests beginning from long error message
        with pytest.raises(ZeroDivisionError, match = "Sum of variance is too small."):
            linfit.fit(x,y,sigma)
