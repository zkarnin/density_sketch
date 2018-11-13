from numpy import outer, dot
from numpy.random import randn
from numpy.linalg import norm

for d in range(221,301):
    for t in range(10):
        n = 1000
        X = randn(n,d)
        S = randn(n)
        for i in range(n):
            X[i,:] = X[i,:]/norm(X[i,:])
            S[i] = 1.0 if S[i] > 0.0 else -1.0 
        
        C = sum(S[i]*outer(X[i,:],X[i,:]))
        curr_norm = norm(C,2)
        for _ in range(10):
            for i in range(1,n):
                change_C = C - 2*S[i]*outer(X[i,:],X[i,:])
                if norm(change_C) < curr_norm:
                    C = change_C
                    S[i] = -1.0 if S[i] > 0.0 else -1.0

        C = sum(S[i]*outer(X[i,:],X[i,:]))
        print('%s,%f'%(d,norm(C,2)))
