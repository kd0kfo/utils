def head(arr, N=5):
    """
    Prints the first N lines of the numpy array.
    """
    
    print(arr[0:N])

def tail(arr, N=5):
    """
    Prints the last N lines of the numpy array.
    """
    
    print(arr[-N:])

def rmse(arr):
    """
    Calculates the RMSE of an array of data.
    """
    import numpy as np
    from math import sqrt

    avg = np.mean(arr)
    return sqrt(np.mean((arr-avg)**2))
    
