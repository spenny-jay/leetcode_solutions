"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        # stores matching original nodes and deep copy nodes
        clones = {}
        clones[node.val] = Node(node.val, [])
        queue = deque([ node ])

        while queue:
            currNode = queue.popleft()
            currClone = clones[currNode.val]
            for neighbor in currNode.neighbors:
                # create new node and add the neighbor we have yet to visit to the queue
                if not neighbor.val in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # update the clone's neighbors list
                currClone.neighbors.append(clones[neighbor.val])

        return clones[node.val]