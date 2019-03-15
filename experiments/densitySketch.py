from numpy import ones, zeros, array
from numpy.linalg import norm
from math import exp

class DensitySketch:
    def __init__(self, vectors, kernel_type='gaussian', kernel_scale=1.0):
        self.vectors = vectors
        self.size = vectors.shape[0]
        self.w = 1.0/float(self.size)
        self.d = vectors.shape[1]
        self.kernel_scale = kernel_scale
        if kernel_type.lower() in ['gaussian','g',0]:
            self.kernel = self.kernel_gaussian
        elif kernel_type.lower() in ['exponential','e',1]:
            self.kernel = self.kernel_exponential
        elif kernel_type.lower() in ['cauchy','c',2]:
            self.kernel = self.kernel_cauchy
        else:
            raise ValueError('kernel_type must be from the follwing values ["gaussian","exponential","cauchy"]')

    # Could be replaced with any positive semidefinite kernel 
    def kernel_gaussian(self, v1,v2, scale=1.0):
        return exp(-(norm(v1-v2)/scale)**2)
    
    def kernel_exponential(self, v1,v2, scale=1.0):
        return exp(-norm(v1-v2)/scale)

    def kernel_cauchy(self, v1,v2, scale=1.0):
        return 1.0/(1.0 + norm(v1-v2)/scale)

    # Computes the density at a point in a really slow way.
    def density(self, vector):
        density_sum = 0.0
        for other in self.vectors:
            density_sum += self.kernel(vector, other, self.kernel_scale)
        return self.w*density_sum

    def split(self):
        s1 = []
        s2 = []
        for i in range(self.size):
            vi = self.vectors[i]
            err = 0.0
            err += sum(self.kernel(vi,vj,self.kernel_scale) for vj in s1)
            err -= sum(self.kernel(vi,vj,self.kernel_scale) for vj in s2)
            if err < 0.0:
                s1.append(vi)
            else:
                s2.append(vi)                
        return (s1,s2)                   

    def compress(self, k=None):
        if k == None:
            k = self.size-1
      
        while self.size > k:
            (s1,s2) = self.split()
            if len(s1)<len(s2):
                self.vectors = array(s1)
            else:
                self.vectors = array(s2)
            self.size = len(self.vectors)
            self.w = 2.0*self.w
            