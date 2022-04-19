# https://leetcode.com/problems/recover-binary-search-tree/submissions/
# Do in order traversal 
# When found first violation assign first and second Tree node
# When found second violation update second Tree Node
# Swap first and second value
# 
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.prev = TreeNode(-2**31,None,None)
        self.first = None
        self.second = None

    def recoverTree(self, root: TreeNode) -> None:
        self.traversal(root)
        self.first.val,self.second.val = self.second.val,self.first.val 
        
        
    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left)
        if root.val < self.prev.val:
            if self.first is None:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.traversal(root.right)
