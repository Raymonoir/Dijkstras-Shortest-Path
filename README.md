# Dijkstras-Shortest-Path

<h1> Background </h1>
As part of my Further Mathematics A-Level I was expected to be able to use and complete Dijkstras Shortest Path algorithm on a graph of ten or more nodes which can be a very lengthy and tough process. <br>

This algorithm begins with the starting node giving it a distance of zero, assigning this to the current node and the rest of the nodes that have not already been travelled to a distance of infinity. The algorithm then goes to each node that connects to the current node, gives it a tempory distance dependant on the current nodes permanent distance and the length of the edge, then picks the smallest value in the non permanent nodes and makes it permanent. This node is made the current node and the process continues until all nodes have been travelled to. 


<h1>Instructions</h1>
 
This implementation of Dijkstras Shortest Path algorithm required a graph to be in the form of a table of values as shown:

   A    B    C    D    E     F   
A [ -1 ,  7 ,  9 , -1 , -1 ,  14 ] <br>
B [  7 , -1 , 10 , 14 , -1 ,  -1 ] <br>
C [  9 , 10 , -1 , 11 , -1 ,   2 ] <br>
D [- 1 , 15 , 11 , -1 ,  6 ,  -1 ] <br>
E [- 1 , -1 , -1 ,  6 , -1 ,   9 ] <br>
F [ 14 , -1 ,  2 , -1 ,  9 ,  -1 ] <br>
  
  
The table is read FROM Column TO Row. The distance is given by the value and a minus one means no direct route is available between the two nodes. <br>

The graph you wish to used must be assigned to a variable and the 'Graph' class must be instantiated with it as a parameter. The program will then output the shortest distance possible to the console.



<h1>Possible additions </h1>
1. User friendly GUI <br>
2. Program records the path of the shortest route

