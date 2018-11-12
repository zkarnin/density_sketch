import numpy
from math import exp, pow
from numpy.linalg import norm
from numpy import array
from random import choice

class DensityCompactor:
    def __init__(self, k):
        self.k = k
        self.size = 0
        self.vectors = []
        self.signs = []

    def kernel(self, vector1, vector2):
        return exp(-pow(norm(vector1-vector2),2))

    def update(self, vector):
        self.vectors.append(vector)
        if self.size > 0:
            x = -sum(s*self.kernel(vector, v) for (s,v) in zip(self.signs, self.vectors))
            sign = 1.0 if x > 0.0 else -1.0
        else:
            sign = choice([1.0, -1.0])
        self.signs.append(sign)
        self.size += 1
            
    def compact(self):
        sketch = []
        for (s,v) in zip(self.signs, self.vectors):
            if s > 0.0:
                sketch.append(v)      
        self.vectors.clear()
        self.signs.clear()
        self.size = 0
        return(sketch)

if __name__ == '__main__':
    from numpy.random import randn 
    d = 20
    k = 100
    dc = DensityCompactor(k)
    points = randn(k,d)
    for p in points:
        dc.update(p)

    sketch = array(dc.compact())
    print(sketch)

            
            
            

        

