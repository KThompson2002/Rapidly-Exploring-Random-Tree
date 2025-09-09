import numpy as np
from node import Node

class KDNode():
    def _init(self, root, nd, align):
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
        if align == 0:
            if child.x < self.x:
                if left is None:
                    child.set_align(1)
                    left = child
                    return self.nd
                else:
                    return left.search(child)
            else:
                if right is None:
                    child.set_align(1)
                    right = child
                    return self.nd
                else:
                    return right.search(child)
        else:
            if child.y < self.y:
                if left is None:
                    child.set_align(0)
                    left = child
                    return self.nd
                else:
                    return left.search(child)
            else:
                if right is None:
                    child.set_align(0)
                    right = child
                    return self.nd
                else:
                    return right.search(child)

    def set_align(align):
        self.align = align