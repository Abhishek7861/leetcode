# Find if given graph is bipartite
# Use 2 colouring method
# run this method for each node as there can be node with no edges and we should traverse all the components 
# 
#


from typing import List


class Solution:
    def __init__(self):
        self.color = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = len(graph)
        for i in range(nodes):
            self.color.append(-1)

        for v in range(nodes):
            queue = [v]
            if self.color[v] == -1:
                self.color[v] = 1
            while len(queue) > 0:
                node = queue.pop(0)
                colour = self.color[node]
                for i in graph[node]:
                    if self.color[i] == colour:
                        print(self.color)
                        return False
                    elif self.color[i] == -1:
                        self.color[i] = 1 - colour
                        queue.append(i)
        return True


obj = Solution()

print(obj.isBipartite(
    [[], [2], [1, 3], [2]]))
