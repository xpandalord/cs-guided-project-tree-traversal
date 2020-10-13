"""
You are given a binary tree.
​
Write a function that can return the inorder traversal of node values.
​
Example:
Input:
​
   3
    \
     1
    /
   5
​
Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
​
def inorder_traversal(root):
    # Your code here
    result = []
    helper(root, result)
    return result 
​
def helper(root, res):
    if root is None:
        return
    
    helper(root.left, res)
    res.append(root.val)
    helper(root.right, res)
​
tree = TreeNode(5)
tree.left = TreeNode(3)
right = TreeNode(32)
right.right = TreeNode(43)
right.left = TreeNode(8)
tree.right = right
​
print(inorder_traversal(tree))