import numpy as np

class Node():
    def __init__(self, root, pt):
        """Define node class initialization"""
        self.point = pt
        self.q_near = []
        self.root = root

    def add_near(self, near):
        self.q_near = np.append(self.q_near, near)

    