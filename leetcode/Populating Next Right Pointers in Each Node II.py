"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
__author__ = 'phoenix'


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = [root]
        next_queue = []
        while len(queue) > 0:
            if queue[0] is None:
                break
            lchild = queue[0].left
            rchild = queue[0].right
            if lchild is not None:
                next_queue.append(lchild)
            if rchild is not None:
                next_queue.append(rchild)
            if len(queue) == 1:
                queue[0].next = None
                queue = next_queue[:]
                next_queue = []
                continue
            queue[0].next = queue[1]
            queue = queue[1:]
        return


if __name__ == '__main__':
    a = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    d = TreeLinkNode(4)
    e = TreeLinkNode(5)
    f = TreeLinkNode(6)
    g = TreeLinkNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    o = Solution()
    o.connect(a)
    print(b.next.val)
    print(e.next.val)
    print(a.next.val)