#Dijkstra in pyhton
import math
"""
     A  B  C  D  E  F 
 A   -  7  9  -  -  14
 B   7  -  10 14 -  -
 C   9  10 -  11 -  2
 D   -  15 11 -  6  -
 E   -  -  -  6  -  9
 F   14 -  2  -  9  -

Shortest Path A-E (20)

-1 or - = Cannot Reach
"""
graphList = [[ -1 ,  7 ,  9 , -1 , -1 ,  14 ],
             [  7 , -1 , 10 , 14 , -1 ,  -1 ],
             [  9 , 10 , -1 , 11 , -1 ,   2 ],
             [- 1 , 15 , 11 , -1 ,  6 ,  -1 ],
             [- 1 , -1 , -1 ,  6 , -1 ,   9 ],
             [ 14 , -1 ,  2 , -1 ,  9 ,  -1 ]]
                
graphList2 = [[-1,6,10,7,-1,-1,-1,-1,-1,-1],
              [6,-1,3,-1,12,-1,-1,-1,-1,-1],
              [10,3,-1,1,8,-1,-1,-1,-1,-1],
              [7,-1,1,-1,10,-1,-1,-1,-1,-1],
              [-1,12,8,10,-1,8,-1,-1,-1,-1],
              [-1,-1,-1,-1,8,-1,10,5,12,-1],
              [-1,-1,-1,-1,-1,10,-1,4,-1,10],
              [-1,-1,-1,-1,-1,5,4,-1,6,15],
              [-1,-1,-1,-1,-1,12,-1,6,-1,4],
              [-1,-1,-1,-1,-1,-1,10,15,4]]

graphList3 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1], 
        [4, -1, 8, -1, -1, -1, -1, 11, -1], 
        [-1, 8, -1, 7, -1, 4, -1, -1, 2], 
        [-1, -1, 7, -1, 9, 14, -1, -1, -1], 
        [-1, -1, -1, 9, -1, 10, -1, -1, -1], 
        [-1, -1, 4, 14, 10, -1, 2, -1, -1], 
        [-1, -1, -1, -1, -1, 2, -1, 1, 6], 
        [8, 11, -1, -1, -1, -1, 1, -1, 7], 
        [-1, -1, 2, -1, -1, -1, 6, 7, -1] 
        ]


startNodeIndex = 0
endNodeIndex = 9
 

class Graph:

    
    def __init__(self,graphList):
        self.nodeList = []
        self.edgeList = []
        
        #Creates nodes and adds to nodeList
        for i in range (0,len(graphList)):
            newNode = Node()
            self.nodeList.append(newNode)

        #Creating the graph, using the nodes to create a list of edges
        for i in range (0,len(graphList)):
            for j in range (0,len(graphList[i])):
                if graphList[i][j] > -1:
                    newEdge = Edge(graphList[i][j], self.nodeList[i], self.nodeList[j])
                    self.edgeList.append(newEdge)
                    self.nodeList[i].addEdge(newEdge)
                    self.nodeList[j].addEdge(newEdge)
                    graphList[j][i] = -1
                   
        D1 = Dijkstra(self.edgeList,self.nodeList,self.nodeList[startNodeIndex],self.nodeList[endNodeIndex])
        D1.startAlgorithm()
        print("Shortest Distance from node" , startNodeIndex , "to" , endNodeIndex , "is" , D1.endNode.distanceFromStart)
        

class Edge:
    def __init__ (self,distance, node1, node2):
        self.nodeList = []
        
        self.distance = distance
        self.nodeList.append(node1)
        self.nodeList.append(node2)

    #Retuns the node on the other end of an edge
    def getConnectingNode(self, givenNode):
        for node in self.nodeList:
            if givenNode == node:
                pass
            else:
                return node
    

class Node:

    def __init__(self):
        self.edgeList = []
        self.distanceFromStart = math.inf
        self.previousNodes = []
        
        
    def addPrevNode(self,node):
        self.previousNodes.append(node)


    def addEdge(self,edge):
        self.edgeList.append(edge)

    
    def setDistance(self,distance):
        self.distanceFromStart = distance
        

class Dijkstra:
    def __init__(self,edgeList,nodeList,startNode,endNode):
        self.startNode = startNode
        self.endNode = endNode
        self.shortestDist = math.inf
        self.unvisitedNodes = nodeList



    def startAlgorithm(self):
        
        self.startNode.setDistance(0)
        currentNode = self.startNode
        self.unvisitedNodes.remove(currentNode)
        currentShortestDistance = math.inf

        while len(self.unvisitedNodes) != 0:

            #For each edge connected to the current node, updating the connected node if the distance is shorter
            for i in range(0,len(currentNode.edgeList)):
                if currentNode.edgeList[i].getConnectingNode(currentNode).distanceFromStart > currentNode.distanceFromStart + currentNode.edgeList[i].distance:
                    currentNode.edgeList[i].getConnectingNode(currentNode).setDistance(currentNode.distanceFromStart + currentNode.edgeList[i].distance)
                    currentNode.edgeList[i].getConnectingNode(currentNode).addPrevNode(currentNode)
                    
            shortestDistanceSoFar = math.inf
            

            #Iteration through each unvisited node to find nect current node
            for i in range (0, len(self.unvisitedNodes)):
                if self.unvisitedNodes[i].distanceFromStart < shortestDistanceSoFar:
                    shortestDistanceSoFar = self.unvisitedNodes[i].distanceFromStart
                    closestNodeSoFar = self.unvisitedNodes[i]

            #Setting current node to the node with the shortest distance from start so far within unvisited nodes list
            currentNode = closestNodeSoFar

            #remove this new current node
            self.unvisitedNodes.remove(currentNode)


if (__name__ == "__main__"):
    G1 = Graph(graphList2)
    






    
    


