
from collections import defaultdict

# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order



class Solution:
    # Your task is to complete this function
    # Function should return Topologically Sorted List
    # Graph(adj) is a list of List
    # V is no of Vertices
    def topoSort(self, V, adj):
        # Code here
        stack=[]
        visited = {}
        for v in range(V):
            visited[v]=0
            
        for v in range(V):
            if(visited[v]==0):
                self.topologicalSort(stack,visited, v, adj[v], adj)
            
        sortList = []
        for i in range(len(stack)):
            sortList.append(stack.pop())
        
        return sortList

    def topologicalSort(self,stack, visited, v, mylist, adj):
        
        visited[v]=1
            
        if(len(mylist)==0):
            stack.append(v)
            return

        for node in mylist:
            if(visited[node]==0):
                self.topologicalSort(stack, visited, node, adj[node], adj)
        
        stack.append(v)


 

 

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    
    print ("Following is a Topological Sort of the given graph")
    
    # Function Call
    #g.topologicalSort()
    
    # This code is contributed by Neelam Yadav


    adj = [[],[3],[3],[],[0,1],[0,2]]
    sol = Solution()
    print(sol.topoSort(6,adj))
