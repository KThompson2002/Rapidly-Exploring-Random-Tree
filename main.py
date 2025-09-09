#!usr/bin/env python3
import numpy as np
from node import Node
from kdnode import KDNode
from kdtree import KDTree
from tree import Tree

def main():
    q_init = Node(None, 50, 50)
    K = 100
    g = Tree(q_init, K, 1, np.array([100, 100]))
    for i in range(K):
        q_rand = g.random_config()
        new_nd = Node(None, 0, 0)
        g.search(new_nd, q_rand)


if __name__ == "__main__":
    main()