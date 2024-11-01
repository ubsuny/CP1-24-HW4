import numpy as np

def dict_maker(v, d):
    sx=np.sum(d)
    sy=np.sum(v)
    d2=[i**2 for i in d]
    sxx=np.sum(d2)
    sxy=0
    
    for count, value in enumerate(v):
        sxy+=value*d[count]
    s=slope(sxx, sy, sx, sxy, len(v))
    b=yint(sxx,sy,sx,sxy,len(v))
    sig=sigma(len(v), s,b, v,d)
    sig_b=sigma_b(sig,sxx, sx, len(v))
    sig_s=sigma_s(sig, len(v),sxx,sx)

    return {"Slope":s, "Y-intercept":b, "Uncertainty of Slope":sig_s, "Uncertainty of y-intercept":sig_b}

def yint(sxx, sy, sx, sxy, n):
    return (sxx*sy-sx*sxy)/(n*sxx-sx**2)

def slope(sxx, sy, sx, sxy, n):
    
    return (n*sxy-sx*sy)/(n*sxx-sx**2)


def sigma(n, s, b, y, x):
    if n<=2:
        return 0
    sum=0
    den=n-2
    for count, value in enumerate(x):
        sum+=(y[count]-(s*value+b))**2

    return np.sqrt(sum/den)

def sigma_b(sig, sxx, sx, n):
    return np.sqrt(sig**2*sxx/(n*sxx-sx**2))

def sigma_s(sig, n, sxx, sx):
    return np.sqrt(sig**2*n/(n*sxx-sx**2))

