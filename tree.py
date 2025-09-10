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
        self.collection = [q_init]
        self.obstacles = (np.array[30, 20, 10], np.array[70, 70, 12], np.array[15, 80, 15], np.array[85, 25, 17]) # np.array[x.center, y.center, radii]

    
    def random_config(self):
        q_rand = np.array([random.uniform(0, self.d[0]), random.uniform(0, self.d[1])])
        # print(f"Random point: {q_rand[0]}, {q_rand[1]}")
        return q_rand

    # def nearest_node(self, q_rand, q_curr):
    #     base = euclid(q_rand, q_curr.point)
    #     for i in len(q_curr.q_near):
    #         if base > euclid(q_curr, q_near[0]) 
        
    def euclid(self, x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

    def set_unit(self, x, y):
        x_dist = x[0] - y[0]
        y_dist = x[1] - y[1]
        mag = self.euclid(x, y)
        return np.array([x_dist / mag, y_dist / mag])

    def it_search(self, q_rand):
        ind = 0
        dist = 100000.0
        for i in range(len(self.collection)):
            tmp_dst = self.euclid(self.collection[i].point, q_rand)
            if tmp_dst < dist:
                ind = i
                dist = tmp_dst
        near_nd = self.collection[ind].point
        new_nd = Node(self.collection[ind], near_nd + self.set_unit(q_rand, near_nd))
        # print(new_nd.point)
        self.collection[ind].add_near(new_nd)
        self.collection.append(new_nd)
        self.k += 1

    # Hybrid kd tree + buffer search algorithm currently not in use
    def kd_search(self, nd, q_rand):
        kdsearch = self.kd.search(nd)
        kd_dist = self.euclid(kdsearch.point, q_rand)
        
        distance = 100000.0
        i = 0
        st = 0
        for item in buffer:
            tmp_dist = self.euclid(item.point, q_rand)
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

    def output(self):
        lines = []
        for i in range(1, self.k):
            srt = tuple((self.collection[i].root.point[0], self.collection[i].root.point[1]))
            end = tuple((self.collection[i].point[0], self.collection[i].point[1]))
            lines.append([srt, end])

        return lines

    def check_collision(start, end, circle):
        """ Checks for collision between a line and a circle
        start - starting point of line
        end - end point of line
        circle - np.array([x_center, y_center, radii])
        """
        center = np.array(circle[0], circle[1])
        d = end - start
        f = start - center

        a - np.dot(d,d)
        b = 2 * np.dot(f, d)
        c = np.dot(f, f) - r**@

        disc = b**2 - 4*a*center #calculate discriminate

        if disc < 0:
            return False

        t1 = (-b - np.sqrt(disc)) / (2*a)
        t2 = (-b + np.sqrt(disc)) / (2*a)

        return (0 <= t1 <= 1) or (0 <= t2 <= 1)

