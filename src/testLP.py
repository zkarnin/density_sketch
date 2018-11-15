from scipy.optimize import linprog
from numpy.random import random
from numpy.linalg import norm
from numpy import eye, ones, zeros, vstack


def findSigns(X):
    (n,d) = X.shape
    A_eq = zeros((d,n))
    for i in range(n):
        A_eq[:,i] = X[i,:]/norm(X[i,:])
    b_eq = zeros(d)
    c =random(n)
    bounds=[(-1.0, 1.0)]*n
    res = linprog(c, A_ub=None, b_ub=None,
                  A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='simplex',
                  callback=None, options={"disp": True})

    alpha = res.x
    s = zeros(n)
    for i in range(n):
        s[i] = 1 if random() < (1+alpha[i])/2 else -1
    return(s)


n = 500
d = 20
data = random((n,d))
for i in range(n):
    data[i] = data[i]/norm(data[i])

s = findSigns(data)
sumNorm = norm(sum([s[i]*data[i] for i in range(n)]))
print('Found sign assignment with total norm of', sumNorm)
