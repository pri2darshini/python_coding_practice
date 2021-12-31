
gr = { "x" : ["z", "u", "a"],
          "y" : ["z", "u", "a"],
          "z" : ["x", "y"],
          "u" : ["x", "y"],
          "v" : ["w", "a"],
          "w" : ["v"],
          "a" : ["x", "y", "v"]
        }

def list_edges(graph):
    edges = []
    for vertex in graph:
        for neighbour in graph[vertex]:
            if {neighbour, vertex} not in edges:
                edges.append({vertex, neighbour})
    return edges


#print(list_edges(gr))

class Graph:

#This class defines undirected graphs

    def __init__(self, gr_dict):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary is used
        """
        if gr_dict == None:
            gr_dict = {}
            
        self.__gr_dict = gr_dict

    def vertices(self):
        """ returns a list of the vertices of the graph """
        return list(self.__gr_dict.keys())

    def edges(self):
        """ returns the list of the edges (= 2-sets) of a graph """
        return self.__list_edges()

    def add_vertex(self, vertex):
        """If the vertex passed by the argument vertex is not in the dictionary
           self.__graph_dict a key "vertex" with empty-list value
        is added to the dictionary. Otherwise, the vertex is already in the
           graph and nothing is done."""
        if vertex not in self.__gr_dict:
            self.__gr_dict[vertex] = []
    
            
    def __list_edges(self):
        """ This method produces the edges of the 
            graph. Edges are represented as sets {k}
            with a single vertex x (a loop on the vertex k), where we
            recall that sets never represent duplicate elements, or two 
            vertices {k,l}. ):
        Here we use two-element sets for the edges as we are working with
            an undiricted graph. 
        """
        
        edges = []
        for vertex in self.__gr_dict:
            for neighbour in self.__gr_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

########################################################################################

    
# Question 1: Removing a node

    def remove_vertex(self,vertex):
        for num in self.__gr_dict.values():
            for node in num:
                if node==vertex:
                    num.remove(node)
        if vertex in self.__gr_dict.keys():
            del self.__gr_dict[vertex]
        else:
            return(" The node is not found")
        return(self.__gr_dict)

# Question 2: Removing a edge
    def remove_edge(self,edge):
        n=edge
        edgeList=[]
        for num in self.__gr_dict.values():
            for node in num:
                if node==n[0] or node==n[1]:
                    num.remove(node)
        return self.__gr_dict
    
        for num in edgeList:
            if{n[0],n[1]} in edgeList:
                edgeList.remove({n[0],n[1]})
            elif {n[1],n[0]} in edgeList:
                edgeList.remove({n[1],n[0]})
        return edgeList
    
# Question 3:Eulerian walk
    def euler_walk(self):
        zero_deg=[]
        odd_deg=[]
        for num in self.__gr_dict.values():
            degree=len(num)
            zero_deg.append(degree)
            if degree%2 != 0:
                odd_deg.append(degree)
        if 0 in zero_deg:
            return("Better stay put where are you now!")
        else:
            if len(odd_deg)==0 or len(odd_deg)==2:
                return("Enjoy your walk!")
            else:
                return("Better stay put where are you now!")
        
# Question 4: Count the number of nodes
    def graph_nodes(self):
        return len(self.__gr_dict.keys())

# Question 5: neighbours and their neighbours
    def neighbours(self,n):
        neighbour=[]
        first_neighbour=[]
        second_neighbour=[]

        for num in self.__gr_dict:
            if num==n:
                neighbour=self.__gr_dict[num]
                for num1 in neighbour:
                    first_neighbour.append(self.__gr_dict[num1])
                for num2 in first_neighbour:
                    for num3 in num2:
                        second_neighbour.append(self.__gr_dict[num3])
                        
        print("The neighbour of node",n,"are ",neighbour)
        print("The neighbours of neighbour",n," are ",first_neighbour)
        print("The next neighbours of neighbour",n,"are",second_neighbour)
        return""
 

#We use the following if-statement to help the execution:
   
if __name__ == "__main__":

    gr = { "x" : ["z", "u", "a"],
          "y" : ["z", "u", "a"],
          "z" : ["x", "y"],
          "u" : ["x", "y"],
          "v" : ["w", "a"],
          "w" : ["v"],
          "a" : ["x", "y", "v"]
        }

    graph = Graph(gr)

print(graph.remove_vertex('v'))
print(graph.remove_edge(('x','y')))
print(graph.euler_walk())
print(graph.graph_nodes())
print(graph.neighbours('a'))

###########################################################################

# Question 1: Matrix multiplication
def matrixMultiplication(mat1,mat2):
    res=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j]+=mat1[i][k]*mat2[k][j]
    return res

# Question 2:Power of matrix

def powerOfMatrix(M,n):
    p=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    if n>1:
        for i in range(n-1):
            if i>0:
                p=matrixMultiplication(p,M)
            else:
                p=matrixMultiplication(M,M)
    else:
        p=M
    return p

#Question 3: Markov chains

import numpy as np
import random as rm
# random markov transition
def random_transition_choice(i, transitions, transitionMatrix_size):
    choice = np.random.choice(range(transitionMatrix_size), replace = True, p = transitionMatrix[i])
        # print(choice)
    return transitions[i][choice]
# markov chain
def markov_chain_path(transitionMatrix,time,initial_state):
    print("Initial State : "+str(initial_state))
    # transitionMatrix = transitionMatrix
    states = [1,2,3]
   # print(transitionMatrix)
        # states = [1,2,3]
    activity= [initial_state]
        # print(activity)
    transitionName = [
            [
                [1,1],
                [1,2],
                [1,3]
            ],
            [
                [2,1],
                [2,2],
                [2,3]
            ],
            [
                [3,1],
                [3,2],
                [3,3]
            ]
        ]
    i = 0
    prob = 1
    while i != time:
            # print(i)
        i += 1
        if initial_state == 1:
            change = random_transition_choice(initial_state-1,transitionName,len(transitionMatrix[initial_state-1]))
                # print(change)
            if change == [1,1] and transitionMatrix[0][0] != 0:
                prob = prob * transitionMatrix[0][0]
                    # initial_state = 1
                activity.append(1)
                continue
            elif change == [1,2] and transitionMatrix[0][1] != 0:
                prob = prob * transitionMatrix[0][1]
                initial_state = 2
                activity.append(2)
                continue
            elif transitionMatrix[0][2] != 0:
                prob = prob * transitionMatrix[0][2]
                initial_state = 3
                activity.append(3)
                continue
        if initial_state == 2:
                # print(i)
            change = random_transition_choice(initial_state-1,transitionName,len(transitionMatrix[initial_state-1]))
                # print(initial_state)
            if change == [2,1] and transitionMatrix[1][0] != 0:
                prob = prob * transitionMatrix[1][0]
                initial_state = 1
                activity.append(1)
                continue
            elif change == [2,2] and transitionMatrix[1][1] != 0:
                prob = prob * transitionMatrix[1][1]
                activity.append(2)
                continue
            elif transitionMatrix[1][2] != 0:
                prob = prob * transitionMatrix[1][2]
                initial_state = 3
                activity.append(3)
                continue
                    # print(transitionMatrix[2][2])
        if initial_state == 3:
            change = random_transition_choice(initial_state-1,transitionName,len(transitionMatrix[initial_state-1]))
            if change == [3,1] and transitionMatrix[2][0] != 0:
                prob = prob * transitionMatrix[2][0]
                initial_state = 1
                activity.append(1)
                continue
            elif change == [3,2] and transitionMatrix[2][1] != 0:
                prob = prob * transitionMatrix[2][1]
                initial_state = 2
                activity.append(2)
                continue
            elif transitionMatrix[2][2] != 0:
                prob = prob * transitionMatrix[2][2]
                activity.append(3)
                continue
            
    print("States taken at each time : "+str(activity))
    print("Final state at time "+str(time)+" : "+str(initial_state))
    print("Probability of the state path taken : "+str(prob))
    return prob

# Question 5:
# markov chain convergence
def markov_chain_convergence_test(transitionMatrix,time,initialDistibution):
    power = powerOfMatrix(transitionMatrix,time)
    result = matrixMultiplication(initialDistibution,power)
    print(result)

###########################################################################################

print(matrixMultiplication([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ],   
      
    [
        [5, 8, 1], 
        [6, 7, 3], 
        [4, 5, 9]
    ] ))

print(powerOfMatrix([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ],2))


transitionMatrix = [[0, 1, 0], [0.5, 0, 0.5], [1, 0, 0]]
print(markov_chain_path(transitionMatrix,3,2))



M1 = [[0, 1, 0], [0.5, 0, 0.5], [1, 0, 0]]
initialDistribution=[[1, 0, 0]]
markov_chain_convergence_test(M1, 1, initialDistribution)
markov_chain_convergence_test(M1, 10, initialDistribution)
markov_chain_convergence_test(M1, 50, initialDistribution)
markov_chain_convergence_test(M1, 100, initialDistribution)
