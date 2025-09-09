import numpy as np

class Node():
    def __init__(self, root, x, y):
        """Define node class initialization"""
        self.point = np.array([x, y])
        self.q_near = []
        self.root = root

    def add_near(self, near):
        self.q_near = np.append(self.q_near, near)

    