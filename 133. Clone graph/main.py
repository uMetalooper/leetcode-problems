from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return
        queue = deque()
        newAdjList = dict()
        queue.append(node)
        # BFS
        while queue:
            n = queue.popleft()
            if n.val not in newAdjList:
                newAdjList[n.val] = set()
            for neighbor in n.neighbors:
                if neighbor.val not in newAdjList: # also a visited hashmap
                    newAdjList[neighbor.val] = set()
                    queue.append(neighbor)
                newAdjList[n.val].add(neighbor.val)
                newAdjList[neighbor.val].add(n.val)
        ans = {}
        for node_val in newAdjList:
            ans[node_val] = Node(node_val)
        for node_val in newAdjList:
            for neighbor_val in newAdjList[node_val]:
                ans[node_val].neighbors.append(ans[neighbor_val])
        return ans[1]

    def cloneGraph2(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
        
graph = [[2,4],[1,3],[2,4],[1,3]]
adjList = {}
for i, adj in enumerate(graph):
    adjList[i+1] = Node(i+1)
for key in adjList:
    for node_val in graph[key-1]:
        adjList[key].neighbors.append(adjList[node_val])

print(adjList)
Solution().cloneGraph2(adjList[1])