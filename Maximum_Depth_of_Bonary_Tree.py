"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
"""

"""
Intuition:
The problem is to find the maximum depth or height of a binary tree. The depth of a node is defined as the number of nodes on the longest path from the node to a leaf. The height of the tree is the depth of the root node. The intuition behind the solution is to recursively calculate the height of the left and right subtrees and return the maximum of these heights plus 1 (to account for the current level).

Approach:
If the root is None, return 0, as the depth of an empty tree is 0.
Recursively calculate the height of the left subtree using self.maxDepth(root.left).
Recursively calculate the height of the right subtree using self.maxDepth(root.right).
Return the maximum of the left and right subtree heights plus 1.

Complexity:

Time complexity:
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. This is because each node is visited once, and the time complexity is linear with respect to the number of nodes.

Space complexity:
The space complexity is O(h), where h is the height of the binary tree. In the worst case, the recursion stack could go as deep as the height of the tree. In a balanced binary tree, the height is O(log n), but in the worst case (skewed tree), it could be O(n) where n is the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1
