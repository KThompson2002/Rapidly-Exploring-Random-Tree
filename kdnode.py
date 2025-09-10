import numpy as np
from node import Node

class KDNode():
    def __init__(self, root, nd, align):
        self.root = root
        self.nd = nd
        self.align = align
        self.left = None
        self.right = None

    # def add_child(self, child):
    #     if align == 0:
    #         if child.x < self.x:
    #             if left is None:
    #                 child.set_align(1)
    #                 left = child
    #             else:
    #                 left.add_child(child)
    #         else:
    #             if right is None:
    #                 child.set_align(1)
    #                 right = child
    #             else:
    #                 right.add_child(child)
    #     else:
    #         if child.y < self.y:
    #             if left is None:
    #                 child.set_align(0)
    #                 left = child
    #             else:
    #                 left.add_child(child)
    #         else:
    #             if right is None:
    #                 child.set_align(0)
    #                 right = child
    #             else:
    #                 right.add_child(child)

    def search(self, child):
        if self.align == 0:
            if child.nd.point[0] < self.nd.point[0]:
                if self.left is None:
                    child.set_align(1)
                    self.left = child
                    return self.nd
                else:
                    return self.left.search(child)
            else:
                if self.right is None:
                    child.set_align(1)
                    self.right = child
                    return self.nd
                else:
                    return self.right.search(child)
        else:
            if child.point[1] < self.nd.point[1]:
                if self.left is None:
                    child.set_align(0)
                    self.left = child
                    return self.nd
                else:
                    return self.left.search(child)
            else:
                if self.right is None:
                    child.set_align(0)
                    self.right = child
                    return self.nd
                else:
                    return self.right.search(child)

    def set_align(align):
        self.align = align