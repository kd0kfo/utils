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
    
def names(_file,delimiter = '\t'):
    """
    Takes a file and maps names in the header line to column indices (zero-indexed)
    """

    infile = _file
    if isinstance(_file,str):
        infile = open(_file,"r")
    header = infile.readline()
    tokens = header.split(delimiter)
    idx = 0
    names = {}
    for token in tokens:
        names[token] = idx
        idx += 1
    return names
