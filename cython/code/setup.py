# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("compute.pyx", compiler_directives={'profile': True,'language_level': "3"}, annotate=True),
    include_dirs=[np.get_include()]  # Add this line to include NumPy headers
)
