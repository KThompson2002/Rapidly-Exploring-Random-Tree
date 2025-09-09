import numpy as np

class Node():
    def __init__(self, x, y)
        """Define node class initialization"""
        self.point = np.array([x, y])
        self.q_near = []

    def add_near(self, near):
        self.q_near = np.append(self.q_near, near)

    