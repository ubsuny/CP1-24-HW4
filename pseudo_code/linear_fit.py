""""
Takes input data in the form of a csv with specified names of headers
and producdes x, y, and errors in y as lists to use for analysis.
Outputs intercept a, slope b, standard deviation of each, and a quality of fit.
"""

import pandas as pd

def read_data_from_csv(filename, x_header='x', y_header='y', sigma_header='sigma'):
    """
    Reads CSV and outputs x, y, and sigma.
    CSV must have headers named 'x','y','sigma' unless specified in input.

    Parameters:
    - filename (str): The path to the CSV file.
    - x_header (str): Header of the column in csv coresponding to x data.
    - y_header (str): Header of the column in csv coresponding to y data.
    - sigma_header (str): Header of the column in csv coresponding to error data.

    Returns:
    - tuple: Three lists containing x, y, and sigma values.

    Defined Errors:
    - Inputs files or headers not strings.
    - CSV unable to be found.
    - Specified headers not in CSV.
    """

    # Checks if input file and headers are strings.
    if not all(isinstance(i, str) for i in [filename, x_header, y_header, sigma_header]):
        raise TypeError("File path and headers must be strings.")
    # Tries to open CSV, if file not found, returns specified error.
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError as exc:
        raise FileNotFoundError("File was not found.") from exc
    # Checks if headers are in CSV columns.
    for i in [x_header, y_header, sigma_header]:
        if i not in df.columns:
            raise KeyError("File headers not found in CSV.")

    x = df[x_header].values.tolist()
    y = df[y_header].values.tolist()
    sigma = df[sigma_header].values.tolist()
    return x, y, sigma

def fit(x, y, sigma):
    """
    Perform a weighted least-squares linear fit to the given data.

    Parameters:
    - x (list): List of x values.
    - y (list): List of y values.
    - sigma (list): List of uncertainty values for y.

    Returns:
    - Dictionary of intercept, slope, error of each, and quality of fit.
    
    Defined Errors:
    - Inputs not lists.
    - Elements of lists not numeric.
    - Fewer x values than y or sigma.
    - Only one datapoint in lists.
    - Error too small (divide by zero)
    - Sum of variance too small (divide by zero)
    """
     # Error Checks:
     # Checks if inputs are lists.
    if not all(isinstance(i, list) for i in [x, y, sigma]):
        raise TypeError("Input not in form of lists.")
    # Checks if elements of lists are numeric.
    if not all(isinstance(i, (int,float)) for groups in [x, y, sigma] for i in groups):
        raise TypeError("Elements of list are not all numeric.")
     # Verifies data are lists of same length.
    if not all(len(i) == len(x) for i in [y, sigma]):
        raise TypeError("Data must be lists of same length.")
    # Makes sure there are at least 2 datapoint to fit.
    if len(x) < 2:
        raise TypeError("Not enough data to fit.")

    n = len(x)
    variance_sum, s_x, s_y = 0.0, 0.0, 0.0

    for i in range(n):
        if abs(sigma[i]) < 0.00001: # Avoids divide by 0 error.
            raise ZeroDivisionError("Element of sigma is too small.")
        variance_sum += 1.0 / sigma[i]**2
        s_x += x[i] * 1.0 / sigma[i]**2
        s_y += y[i] * 1.0 / sigma[i]**2

    s_tt, b = 0.0, 0.0

    for i in range(n):
        t_i = 1.0 / sigma[i] * (x[i] - s_x / variance_sum)
        s_tt += (t_i)**2
        b += (t_i * y[i]) / sigma[i]

    if abs(variance_sum) < 0.000001: # Avoids divide by 0 error.
        raise ZeroDivisionError("Sum of variance is too small.")

    # Calculate slope and intercept of fit:
    b /= s_tt
    a = (s_y - s_x * b) / variance_sum
    # Calculate standard deviation of slope and intercept:
    sigma_a = (1 + s_x**2 / (variance_sum * s_tt))**0.5 / variance_sum**0.5
    sigma_b = (1.0 / s_tt)**0.5

    # Calculate quality of fit:
    chi2 = sum(((y[i] - a - b * x[i]) / sigma[i])**2 for i in range(n))

    return {
        'intercept': a,
        'slope': b,
        'sigma_a': sigma_a,
        'sigma_b': sigma_b,
        'chi_squared': chi2
    }

# Usage example.
# Only runs example if module is ran directly as a script.
# Avoids error output in unit testing.
# Do not need to use if name == main when using functions in another document.
if __name__ == "__main__":
    FILENAME = 'data.csv'
    X, Y, SIGMA = read_data_from_csv(FILENAME)
    result = fit(X, Y, SIGMA)
    print("Results:", result)
