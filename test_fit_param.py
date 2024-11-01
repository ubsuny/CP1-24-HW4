"""
test_fit_params acts as a module to use 
with pytest in the command line such that 
the functionality of the fit_param module 
may be confirmed. 
"""
from fit_param import dict_maker

def test_dict_maker():
    """
    This test ensures that dict_maker correctly 
    calculates slope, y-intercept, and their
    uncertainties. The x, y axis and results 
    that I want my parameters to be equal to
    are based off of excel calculations with
    the linest function.
    """
    x=[203,303,505,607,704]
    y=[944,1320,2300,2790,3200]
    params=dict_maker(y,x)
    assert round(params["Slope"],4)==4.5931
    assert round(params["Y-intercept"],3)==-22.225
    assert round(params["Uncertainty of Slope"],6)==.090975
    assert round(params["Uncertainty of y-intercept"],5)==45.52561

def test_bad_data():
    """
    This test ensures that the dict_maker function
    may run even if a dataset that can't be fitted 
    is input.
    """
    x=[1,2,3,4]
    y=[1,2]
    assert dict_maker(y,x)==0
    x=[0]
    y=[0]
    assert dict_maker(y,x)==0
    x=[0,0,0,0]
    y=[0,0,0,0]
    assert dict_maker(y,x)==0