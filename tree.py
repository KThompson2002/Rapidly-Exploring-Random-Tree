import numpy as np
import random
import math
from node import Node
from kdtree import KDTree
from collections import deque

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
        self.k = 1
        self.u = u
        self.d = d
        self.kd = KDTree(q_init)
        self.buffer_lim = (int)(K/10)
        self.buffer = deque([])

    
    def random_config(self):
        q_rand = np.array([random.uniform(0, self.d[0]), random.uniform(0, self.d[1])])
        return q_rand

    # def nearest_node(self, q_rand, q_curr):
    #     base = euclid(q_rand, q_curr.point)
    #     for i in len(q_curr.q_near):
    #         if base > euclid(q_curr, q_near[0]) 
        
    def euclid(self, x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]+y[1])**2)

    def set_unit(self, x, y):
        x_dist = x[0] - y[0]
        y_dist = x[1] - y[1]
        mag = euclid(x, y)
        return np.array([x_dist / mag, y_dist / mag])

    def search(self, nd, q_rand):
        kdsearch = self.kd.search(nd)
        kd_dist = euclid(kdsearch.point, q_rand)
        
        distance = 100000.0
        i = 0
        st = 0
        for item in buffer:
            tmp_dist = euclid(item.point, q_rand)
            if (tmp_dist < distance):
                distance = tmp_dist
                st = i
            i += 1
        
        if tmp_dst < kd_dist:
            nd.point = buffer([i]).point + set_unit(q_rand, buffer([i]).point)
            nd.root = buffer([i])
            buffer([i]).add_near(nd)
        else:
            nd.point = kdsearch([i]).point + set_unit(q_rand, kdsearch([i]).point)
            nd.root = kdsearch
            kdsearch.add_near(nd)

        buffer.append(root)
        if len(buffer) >= buffer_lim:
            buffer.popleft()
