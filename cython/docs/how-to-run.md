# How to Run

## Intro
The compute.pyx module calculates the chi squared value using an input of 3 numpy arrays (x, y, and sigma). Since it uses cython, it must first be compiled.

First make sure you have cython and setuptools installed:
```bash
pip install --upgrade setuptools cython
```

There is a setup.py file provided, to compile it run:
```bash
python -m setup build_ext --inplace
```

This will produce a new file called `compute.pyd` which can be imported as a python module, as well as an analysis document named `compute.html` (which can also be found in the /docs/ directory) which highlights the lines of code that utilize the most time/resources.

## Usage
Once its compiled, the module can be imported with:
```python
import compute
```
With the module imported, you can use it like a normal python object:
```Python
# basic imports
import numpy as np
import random

# Create some arrays from 0 to 1 with 10 as the values
x = np.linspace(1, random.uniform(1.0, 500.0), 10000000)
y = np.linspace(1, random.uniform(1.0, 500.0), 10000000)
sigma = np.linspace(1, random.uniform(1.0, 500.0), 10000000)

chi = compute.compute_with_cython(x,y,sigma)

print(chi)
```

## Performance
The module can be profiled by running
```bash
python profiler.py
```
which will log the results to a `profiling_results.txt`. The profiling process can be tailored by altering the `profiler.py` module.

Profiling tests yield a runtime of 1.346s for computing against 3 np arrays with 1e7 elements each.
