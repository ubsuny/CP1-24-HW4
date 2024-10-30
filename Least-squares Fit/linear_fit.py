import pandas as pd

def read_data_from_csv(filename):
    """
    Reads x, y, and sigma values from a CSV file.
    
    Parameters:
        filename (str): The path to the CSV file.
        
    Returns:
        tuple: Three lists containing x, y, and sigma values.
    """
    df = pd.read_csv(filename)
    x = df['x'].tolist()
    y = df['y'].tolist()
    sigma = df['sigma'].tolist()
    return x, y, sigma

def linear_fit(x, y, sigma):
    """
    Perform a weighted least-squares linear fit to the given data.

    Parameters:
        x (list): List of x values.
        y (list): List of y values.
        sigma (list): List of sigma (uncertainty) values for y.

    Returns:
        dict: A dictionary with keys 'intercept' (a), 'slope' (b), 'sigma_a', 'sigma_b', and 'chi_squared'.
              Returns None if the fit cannot be performed due to insufficient data or invalid sigma values.
    """
    n = len(x)
    if n < 2:
        print('Error! Not enough data!')
        return None
    
    S, s_x, s_y = 0.0, 0.0, 0.0
    
    for i in range(n):
        if abs(sigma[i]) < 0.00001:
            print("Error! sigma_i is too small.")
            return None
        weight = 1.0 / sigma[i]**2
        S += weight
        s_x += x[i] * weight
        s_y += y[i] * weight

    s_tt, b = 0.0, 0.0
    for i in range(n):
        weight = 1.0 / sigma[i]
        t_i = weight * (x[i] - s_x / S)
        s_tt += t_i**2
        b += t_i * y[i] * weight
    
    if abs(S) < 0.000001:
        print("Error! S is too small.")
        return None

    b /= s_tt
    a = (s_y - s_x * b) / S
    sigma_a = (1 + s_x**2 / (S * s_tt))**0.5 / S**0.5
    sigma_b = (1.0 / s_tt)**0.5
    
    chi2 = sum(((y[i] - a - b * x[i]) / sigma[i])**2 for i in range(n))
    
    return {
        'intercept': a,
        'slope': b,
        'sigma_a': sigma_a,
        'sigma_b': sigma_b,
        'chi_squared': chi2
    }

# Usage example
filename = 'data.csv'
x, y, sigma = read_data_from_csv(filename)
result = linear_fit(x, y, sigma)
print("Results:", result)
