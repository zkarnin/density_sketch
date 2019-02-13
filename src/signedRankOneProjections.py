from numpy import outer, dot, zeros, sum
from numpy.random import randn, random, randint
from numpy.linalg import norm


for d in range(1,101):
    for t in range(1):
        n = 10000
        #X = random((n,d))
        #X = randn(n,d)
        X = zeros((n,d))
        S = zeros(n)
        C = zeros((d,d))
        for i in range(n):
            #x = random(d)
            #x = randn(d)
            x = zeros(d)
            x[randint(0,d)] =  1.0
            x[randint(0,d)] = -1.0
            x = x/norm(x)
            X[i,:] = x
            S[i] = 1.0 if random() > 0.5 else -1.0 
            C += S[i]*outer(X[i],X[i])

        curr_norm = norm(C,2)
        sign_changes_list = [0]
        norm_list = [curr_norm]
        sign_changes = 1
        while sign_changes > 0:
            sign_changes = 0
            for i in range(1,n):
                change_C = C - 2*S[i]*outer(X[i,:],X[i,:])
                change_norm = norm(change_C,2)
                if change_norm < curr_norm:
                    C = change_C
                    curr_norm = change_norm
                    S[i] = -1.0 if S[i] > 0.0 else 1.0
                    sign_changes+=1
                    
            sign_changes_list.append(sign_changes)
            norm_list.append(curr_norm)
            
        final_C = sum(S[i]*outer(X[i,:],X[i,:]) for i in range(n))
        final_norm = norm(final_C,2)
        s = ' ,'.join('%d, %f'%(sc, cn) for (sc, cn) in zip(sign_changes_list ,norm_list))
        print('%s, %f, '%(d,final_norm) + s)
