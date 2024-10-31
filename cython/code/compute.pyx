"""
This module defines the function optimized with Cython for fast numerical computations
on NumPy arrays. The function handles potential errors and returns either a dictionary
containing computed values or an error indicator. Specifically, it processes input arrays
to perform calculations and supports returning detailed results or error information,
depending on the success of execution.

Dependencies:
    - numpy: Used for handling array operations efficiently.
    - typing: For type annotations in the function signature.
"""


import numpy as np
cimport numpy as np
from typing import Dict

# Compute with Cython
# This function returns a double OR None if there is an error
# (note the use of the typing module)
def compute_with_cython(
    np.ndarray[np.float64_t, ndim=1] x,
    np.ndarray[np.float64_t, ndim=1] y,
    np.ndarray[np.float64_t, ndim=1] sigma
    ) -> Dict[str, float]:
    """
       Processes input arrays x, y, and params with optimized Cython performance,
       performing calculations and returning results or an error indicator.

       Args:
           x (np.ndarray[np.float64_t, ndim=1]): 1D array of float values representing
               the primary dataset for processing.
           y (np.ndarray[np.float64_t, ndim=1]): 1D array of float values representing
               secondary data to complement x in computations.
           params (np.ndarray[np.float64_t, ndim=1]): 1D array of float values containing
               parameters used to modulate or control the calculations applied to x and y.

       Returns:
           Dict[str, np.ndarray]: A dictionary containing computed values based on x, y,
               and params if successful, or an error dictionary with a sentinel value of -1
               under the key "e" to signal an error during execution.

       Raises:
           ValueError: If input arrays have mismatched lengths or do not meet processing
               requirements.
       """
    # Get the length of the array
    cdef int n = x.shape[0]

    # Check that it has more than 2 elements
    if n < 2:
        print("Error! Not enough data!")
        return {"error": -1}
    # make sure the arrays are the same size
    if n != y.shape[0]:
        print("Error! Data length mismatch!")
        return {"error": -1}

    # Define some vars for the first loop
    cdef double S = 0.0
    cdef double s_x = 0.0
    cdef double s_y = 0.0

    # Define some vars for the second loop
    cdef double t_i = 0.0
    cdef double s_tt = 0.0
    cdef double b = 0.0          # slope

    # Define post-loop vars
    cdef double a = 0.0          # intercept
    cdef double sigma_a = 0.0
    cdef double sigma_b = 0.0
    cdef double chi2 = 0.0       # chi SQUARED

    # first loop
    for i in range(x.shape[0]):
        # make sure sigma is large enough
        if abs(sigma[i]) < 0.00001:
            print("Error! Sigma too small!")
            return {"error": -1}
        # Compound values
        S += 1.0 / sigma[i]**2
        s_x += x[i] / sigma[i]**2
        s_y += y[i] / sigma[i]**2

    # second loop
    for i in range(x.shape[0]):
        t_i = (1.0 / sigma[i]) * (x[i] - (s_x / S))
        s_tt += t_i**2
        b += (t_i * y[i]) / sigma[i]

    # Check error size
    if abs(S) < 0.000001:
        print("Error! Error too small!")
        return {"error": -1}

    # compute a, b, and sigmas
    b = b / s_tt
    a = (s_x - s_y * b) / S
    sigma_a = ((1 + s_x**2 / (S * s_tt)) / S)**0.5
    sigma_b = (1.0 / s_tt)**0.5

    # compute chi2
    for i in range(x.shape[0]):
        chi2 += ((y[i] - a - b * x[i]) / sigma[i])**2

    # Return the computed values
    return {
        'intercept': a,
        'slope': b,
        'sigma_a': sigma_a,
        'sigma_b': sigma_b,
        'chi_squared': chi2
    }
