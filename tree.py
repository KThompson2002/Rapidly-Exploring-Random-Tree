import numpy as np
import random
import math

class Tree():
    def __init__(self, q_init, K, u, d):
        """Initialize tree class
        q_init: initial node position
        K = Final number of verticies
        k = current number of verticies
        u = velocity of exploration
        d = domain size
        """
        self.q_init = q_init
        self.K = K
        k = 1
        self.u = u

    
    def random_config(self):
        q_rand = np.array([random.random(0, d[0]), random.random(0, d[0])])
        return q_rand

    def nearest_node(self, q_rand, q_curr):
        base = euclid(q_rand, q_curr)
        for i in len(q_curr.q_near):
            if base > euclid(q_curr, q_near[0]) 
        
    def euclid(x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]+y[1])**2)