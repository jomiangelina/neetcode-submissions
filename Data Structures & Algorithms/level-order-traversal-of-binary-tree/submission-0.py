# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        # this is an edge case if there is no node 

        result = []
        # we are creating the list of the levels 

        queue = deque([root])
        # creating the deque since it has a faster lookup compared to a list
        # initializing it with the root
        
        while queue: 
            # traversing through the queue 
            level_size = len(queue)
            # seeing how long the current queue is so that we dont go out of bounds
            level = []
            # what is in the level right now?

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                # since this is a queque first in first out, so we add the nodes on the left first since they came first and thats why this also works 

                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # both of the above are seeing the if the current node has children and then adding that 
            result.append(level)
            # again adding that to the result and then in order to return it 
        return result
