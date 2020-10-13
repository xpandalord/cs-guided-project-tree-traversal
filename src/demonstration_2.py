"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
​
*Note: assume that there will not be any duplicates in the tree.*
​
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
​
Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
​
def build_tree(preorder, inorder):
    # Your code here
    preorder_index = 0
​
    # init a dict mapping each value in `inorder` with its index so
    # that we can easily find it 
    index_map = {val: index for index, val in enumerate(inorder)}
    
    # initial call to our recursive helper function
    return helper(preorder, preorder_index, index_map, 0, len(inorder) - 1)[0]
​
def helper(preorder, preorder_index, index_map, inorder_start, inorder_end):
    # base case: when we've gone through the entire `inorder` list of elements
    if inorder_start > inorder_end:
        return None, preorder_index
​
    # init the TreeNode with the root
    root_val = preorder[preorder_index]
    root = TreeNode(root_val)
​
    # the root for the next recursive call will be the next element in `preorder`
    preorder_index += 1
​
    # fetch the root values index from the `index_map`
    root_index = index_map[root_val]
​
    # the left subtree will consist of all elements in `preorder` to the left of the root element
    root.left, preorder_index = helper(preorder, preorder_index, index_map, inorder_start, root_index - 1)
​
    # the right subtree will consist of all elements in `preorder` to the right of the root element
    root.right, preorder_index = helper(preorder, preorder_index, index_map, root_index + 1, inorder_end)
​
    return root, preorder_index
​
def inorder_helper(root, res):
    if root is None:
        return
    inorder_helper(root.left, res)
    res.append(root.val)
    inorder_helper(root.right, res)
​
def inorder_traversal(root):
    result = []
    inorder_helper(root, result)
    return result
​
def preorder_helper(root, res):
    if root is None:
        return
    res.append(root.val)
    preorder_helper(root.left, res)
    preorder_helper(root.right, res)
​
def preorder_traversal(root):
    result = []
    preorder_helper(root, result)
    return result
​
if __name__ == "__main__":
    preorder = [5,7,22,13,9]
    inorder = [7,5,13,22,9]
​
    tree = build_tree(preorder, inorder)
​
    preorder_output = preorder_traversal(tree)
    inorder_output = inorder_traversal(tree)
​
    print("Preorder output matches:", preorder_output == preorder)
    print("Inorder output matches:", inorder_output == inorder)