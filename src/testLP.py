from scipy.optimize import linprog
from numpy.random import random
from numpy.linalg import norm
from numpy import eye, ones, zeros, vstack, dot, outer


def findSigns1(X):
    (n,d) = X.shape
    A_eq = zeros((d,n))
    for i in range(n):
        A_eq[:,i] = X[i,:]/norm(X[i,:])
    b_eq = zeros(d)
    c = ones(n) #random(n)
    bounds=(-1.0, 1.0)
    res = linprog(c, A_ub=None, b_ub=None,
                  A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='simplex',
                  callback=None, options={"disp": True})

    alpha = res.x
    print('alpha', alpha)
    s = zeros(n)
    for i in range(n):
        s[i] = 1 if random() < (1+alpha[i])/2 else -1
    return(s)


def findSigns2(X):
    (n,d) = X.shape
    A_eq = zeros((d**2,n))
    for i in range(n):
        z = X[i,:]/norm(X[i,:])
        A_eq[:,i] = outer(z,z).reshape(d**2)
    b_eq = zeros(d**2)
    c = ones(n) #random(n)
    bounds=(-1.0, 1.0)
    res = linprog(c, A_ub=None, b_ub=None,
                  A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='simplex', #  'simplex' or ‘interior-point’
                  callback=None, options={"disp": True}
                  )

    alpha = res.x
    print('alpha', alpha)
    fractional = sum([1  for a in alpha if a>-0.9999 and a<0.9999 ])
    print('fractional', fractional)
    s = zeros(n)
    for i in range(n):
        s[i] = 1 if random() < (1+alpha[i])/2 else -1
    return(s)


def signedCov(X):
    (n,d) = X.shape
    C = zeros((d,d))
    for i in range(n):
        X[i,:] = X[i,:]/norm(X[i,:])
    C = outer(X[0],X[0])
    for i in range(2,n):
        np = norm(C + outer(X[i],X[i]),2)
        nm = norm(C - outer(X[i],X[i]),2)
        if np < nm:
            C += outer(X[i],X[i])
        else:
            C -= outer(X[i],X[i])
    return(C)


n = 5000
d = 50
data = random((n,d))
for i in range(n):
    data[i] = data[i]/norm(data[i])
#s = findSigns1(data)
#s = findSigns2(data)
#cov = sum([s[i]*outer(data[i],data[i]) for i in range(n)])

cov = signedCov(data)
print('cov norm', norm(cov,2))
#print(list(zip(s1,s2)))
#sumNorm = norm(sum([s[i]*data[i] for i in range(n)]))
#print('Found sign assignment with total norm of', sumNorm)
