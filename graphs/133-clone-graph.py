# LINK: https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Keep track of the original graph nodes and their created deep copy
        visited = {}
        if not node: return None

        def dfs(node):
            # if we already visited this node, return its respective copy we made
            if node in visited:
                return visited[node]
            # otherwise create a new node
            copy = Node(node.val)
            # register it with its original node if we ever revisit it
            # when traversing a node's neighbors
            visited[node] = copy
            # traverse through the node's neighbors and assign them to the new node
            for neighbor in node.neighbors:
                copyNeighbor = dfs(neighbor)
                copy.neighbors.append(copyNeighbor)

            return copy

        return dfs(node)