def linear_fit(data):
    n = len(data)
    if n < 2:
        print('Error! Not enough data!')
        return
    
    S = 0.0
    s_x = 0.0
    s_y = 0.0
    
    # First loop for S, s_x, s_y
    for i in range(n):
        x_i, y_i, sigma_i = data[i]
        if abs(sigma_i) < 0.00001:
            print("Error! sigma_i is too small.")
            return
        S += 1.0 / sigma_i**2
        s_x += x_i / sigma_i**2
        s_y += y_i / sigma_i**2

    # Second loop for t_i, s_tt, and b
    s_tt = 0.0
    b = 0.0
    for i in range(n):
        x_i, y_i, sigma_i = data[i]
        t_i = 1.0 / sigma_i * (x_i - s_x / S)
        s_tt += t_i**2
        b += t_i * y_i / sigma_i
    
    # Check if S is too small
    if abs(S) < 0.000001:
        print("Error! S is too small.")
        return
    
    # Compute slope (b) and intercept (a)
    b = b / s_tt
    a = (s_y - s_x * b) / S
    
    # Calculate error estimates for a and b
    sigma_a2 = (1 + s_x**2 / (S * s_tt)) / S
    sigma_b2 = 1.0 / s_tt
    
    # Compute chi-squared
    chi2 = 0.0
    for i in range(n):
        x_i, y_i, sigma_i = data[i]
        chi2 += ((y_i - a - b * x_i) / sigma_i)**2
    
    return a, b, sigma_a2, sigma_b2, chi2

# Test the function with sample data
test_data = [(1, 2, 0.1), (2, 3, 0.1), (3, 4, 0.1)]
result = linear_fit(test_data)
print("Results:", result)
