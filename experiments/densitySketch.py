from numpy import ones, zeros, array
from numpy.linalg import norm
from math import exp

class DensitySketch:
    def __init__(self, vectors):
        self.vectors = vectors
        self.n = vectors.shape[0]
        self.d = vectors.shape[1]
        self.weights = ones(self.n)

    # Could be replaced with any positive semidefinite kernel 
    def kernel(self, v1,v2, scale_lambda=1.0):
        return exp(-(norm(v1-v2)/scale_lambda)**2)

    # Computes the density at a point in a really slow way.
    def density(self, vector):
        density_sum = 0.0
        for i in range(self.n):
            density_sum += self.weights[i]*self.kernel(self.vectors[i],vector)
        return density_sum/self.n

    def coreset(self):
        s_pos = []
        s_neg = []
        for i in range(self.n):
            vi = self.vectors[i]
            err = 0.0
            err += sum(self.kernel(vi,vj) for vj in s_pos)
            err -= sum(self.kernel(vi,vj) for vj in s_neg)
            if err >= 0.0:
                s_neg.append(vi)
            else:
                s_pos.append(vi)
                                
        if len(s_pos)<len(s_neg):
            return array(s_pos)
        else:
            return array(s_neg)
