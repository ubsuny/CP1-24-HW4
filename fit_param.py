"""
the fit_param module contains functions which together
allow the user to specify velocity and distance data such
that best fit parameters may be calculated. The parameters
are output as a dictionary with keys: "Slope", "Y-intercept",
"Uncertainty of Slope", "Uncertainty of y-intercept"
"""

import numpy as np

def dict_maker(v, d):
    """
    dict_maker takes in velocity and 
    position data as two lists and 
    calls other functions to determine the
    parameters which are returned as a 
    dictionary
    """
    #Invalid datasets are accounted for here.
    if len(v)!=len(d):
        print("Invalid Dataset. Try again")
        return 0
    if len(v)<2:
        print("Not enough data for a fit. Try again")
        return 0


    sx=np.sum(d)
    sy=np.sum(v)
    d2=[i**2 for i in d]
    sxx=np.sum(d2)
    sxy=0

    #If an invalid denominator which is used for 
    #future calculations is determined, the function
    #stops.
    if len(v)*sxx-sx**2==0:
        print("Error. Denominator is 0")
        return 0
    
    for count, value in enumerate(v):
        sxy+=value*d[count]

    s=slope(sxx, sy, sx, sxy, len(v))
    b=yint(sxx,sy,sx,sxy,len(v))
    sig=sigma(len(v), s,b, v,d)
    sig_b=sigma_b(sig,sxx, sx, len(v))
    sig_s=sigma_s(sig, len(v),sxx,sx)

    return {"Slope":s, "Y-intercept":b, "Uncertainty of Slope":sig_s, "Uncertainty of y-intercept":sig_b}

def yint(sxx, sy, sx, sxy, n):
    """
    yint produces the y-intercept from
    sxx,sy, sx, sxy, n
    """
    return (sxx*sy-sx*sxy)/(n*sxx-sx**2)

def slope(sxx, sy, sx, sxy, n):
    """
    slope produces the slope from
    sxx,sy, sx, sxy, n
    """
    return (n*sxy-sx*sy)/(n*sxx-sx**2)


def sigma(n, s, b, y, x):
    """
    sigma, which is necessary for calculating
    uncertainties is determined from n, s, b,
    y, x. s and b are slope and y-intercept 
    respectively, y and x are velocity and distance
    data respectively.
    """
    #Ensures that if n<=2, sigma is zero
    if n<=2:
        return 0
    
    sum=0
    den=n-2
    for count, value in enumerate(x):
        sum+=(y[count]-(s*value+b))**2

    return np.sqrt(sum/den)

def sigma_b(sig, sxx, sx, n):
    """
    sigma_b is determined from sig (sigma), 
    sxx, sx, n
    """
    return np.sqrt(sig**2*sxx/(n*sxx-sx**2))

def sigma_s(sig, n, sxx, sx):
    """
    sigma_s is determined from sig (sigma), 
    sxx, sx, n
    """
    return np.sqrt(sig**2*n/(n*sxx-sx**2))

