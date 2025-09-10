#!usr/bin/env python3
import numpy as np
from node import Node
from kdnode import KDNode
from kdtree import KDTree
from tree import Tree
import matplotlib.pyplot as plt

from matplotlib.collections import LineCollection

def main():
    # doing the interconnect guy
    q_init = Node(None, np.array([50, 50]))
    K = 500
    d = np.array([100, 100])
    g = Tree(q_init, K, 1, d)
    for i in range(K):
        q_rand = g.random_config()
        g.it_search(q_rand)
    
    # printing the guy
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    line_collection = LineCollection(g.output())
    ax.add_collection(line_collection)

    for item in g.collection:
        ax.scatter(item.point[0], item.point[1], c='blue', s=5)

    plt.show()




if __name__ == "__main__":
    main()