import numpy as np
from kdnode import KDNode
from node import Node

class KDTree():
    def __init__(self, nd):
        self.q_init = KDNode(None, nd, 0)

    def search(self, new_nd):
        return self.q_init.search(KD_Node(q_init, new_nd, 0))
        
    

