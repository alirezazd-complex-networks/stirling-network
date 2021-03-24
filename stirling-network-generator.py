import math
import numpy
import networkx as nx
%matplotlib inline
import matplotlib.pyplot as plt

def stirling(n,k):		#Recursive function for generating Stirling numbers of the first kind
    if(n==k):
        return 1
    elif(n==0 or k==0):
        return 0
    else:
        return((n-1)*stirling(n-1,k)+stirling(n-1,k-1))


order = int(raw_input("enter order of graph: "))
order+=1		#increment the order 
SM = numpy.zeros((order,order),dtype= int)
for i in range (order):
    for j in range (i+1):
        SM[i,j]=stirling(i,j)

#Delete first row & column of the table for generating adjacency matrix
SM = numpy.delete(SM,0,0)
SM = numpy.delete(SM,0,1) 



SG = nx.Graph()		#Stirling graph
for i in range(1,order):
    SG.add_node(i)		#Add nodes to the graph
BSM = numpy.zeros((order-1,order-1),dtype= int)
for i in range (order-1):
    for j in range (i+1):
        BSM[i,j] = SM[i-1,j]%2		#Generate adjacency matrix
        BSM[j,i] = BSM[i,j]
        if (BSM[i,j] == 1):
            SG.add_edge(i+1,j+1)		#Add edges to the graph according to adjacency matrix
      
print BSM
nx.draw_networkx(SG,node_color='green',node_size=700)


