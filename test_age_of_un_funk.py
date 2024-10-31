"""Test functions for the age calculation module.

This module contains unit tests for the 'age' function 
from the 'age_of_un_funk' module, which calculates 
the age of the universe based on Hubble's constant.
"""

import pytest
from age_of_un_funk import age

def test_age():
    """ unit test for age function"""
    result = age(70)
    assert pytest.approx(result, rel=1e-5) == 4.4143e+17 #test_age_of_un_funk.py