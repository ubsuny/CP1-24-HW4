# profile_examples.py
import cProfile
import pstats
# Import the cython function
from compute import compute_with_cython
# get numpy
import numpy as np
import random

# create some mock data, use 1e7 data points
x = np.linspace(1, random.uniform(1.0, 500.0), 10000000)
y = np.linspace(1, random.uniform(1.0, 500.0), 10000000)
sigma = np.linspace(1, random.uniform(1.0, 500.0), 10000000)

# In this profile we will:
def run_profile():
    # call the function
    compute_with_cython(x, y, sigma)

# Profile and print statistics saved to file
cProfile.run('run_profile()', 'output.prof')

# Print profiling results to terminal
with open("profiling_results.txt", "w") as f:
    p = pstats.Stats('output.prof', stream=f)
    # List the top 10 results
    p.strip_dirs().sort_stats('cumulative').print_stats(10)

print("Profiling complete. Results saved to profiling_results.txt.")
