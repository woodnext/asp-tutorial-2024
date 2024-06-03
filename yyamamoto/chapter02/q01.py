import math

def dft(x):
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * math.exp(-1j*2*math.pi*k*n/N)
    return X

def idft(X):
    N = len(X)
    x = [0] * N
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * math.exp(1j*2*math.pi*k*n/N) / N
    return x