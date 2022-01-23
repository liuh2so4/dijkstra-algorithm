from tkinter import N
from turtle import color
import matplotlib.pyplot as plt
import random
def edgeLim(x) :
	if x % 20 == 0 :
		return 10
	elif x % 5 == 0 :
		return 5
	else :
		return 3


nodes = {}

# set random nodes
for i in range(0, 100) :
	for j in range(0, 2) :
		nodes[i, j] = random.randint(0, 2000)

# set nodes with different importance in the dijkstra graph
plt.scatter(nodes[0, 0], nodes[0, 1], label = "Primate cities", color = "red", marker = "^", s = 35)
plt.scatter(nodes[5, 0], nodes[5, 1], label = "Cities", color = "orange", marker = "o", s = 30)
plt.scatter(nodes[1, 0], nodes[1, 1], label = "Countries", color = "blue", marker = "*", s = 20)
for i in range(0, 100) :
	if i % 20 == 0 :
		plt.scatter(nodes[i, 0], nodes[i, 1], color = "red", marker = "^", s = 35)
	elif i % 5 == 0 :
		plt.scatter(nodes[i, 0], nodes[i, 1], color = "orange", marker = "o", s = 30)
	else :
		plt.scatter(nodes[i, 0], nodes[i, 1], color = "blue", marker = "*", s = 20)

edges = {}
cntedge = 0
edgerecord = {}
edgelim = {}
for i in range(0, 100) :
	edgelim[i] = 0

# set edges with rules
for i in range(0, 100) :
	if i % 20 == 0 :
		for j in range(i+1, 100) :
			if (j % 20 == 0 and (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 1000000) or (j % 5 == 0 and (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 250000) or (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 50000 :
				if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
					edges[cntedge, 0] = [nodes[i, 0], nodes[j, 0]]
					edges[cntedge, 1] = [nodes[i, 1], nodes[j, 1]]
					edgerecord[cntedge] = [i, j]
					cntedge+=1
					edgelim[i]+=1
					edgelim[j]+=1
				elif edgelim[j] < edgeLim(j) :
					continue
				else :
					break
	elif i % 5 == 0 :
		for j in range(i+1, 100) :
			if j % 5 == 0 and (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 1000000 or (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 250000 :
				if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
					edges[cntedge, 0] = [nodes[i, 0], nodes[j, 0]]
					edges[cntedge, 1] = [nodes[i, 1], nodes[j, 1]]
					edgerecord[cntedge] = [i, j]
					cntedge+=1
					edgelim[i]+=1
					edgelim[j]+=1
				elif edgelim[j] < edgeLim(j) :
					continue
				else :
					break
	else :
		for j in range(i+1, 100) :
			if (nodes[i, 0] - nodes[j, 0]) * (nodes[i, 0] - nodes[j, 0]) + (nodes[i, 1] - nodes[j, 1]) * (nodes[i, 1] - nodes[j, 1]) <= 360000 :
				if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
					edges[cntedge, 0] = [nodes[i, 0], nodes[j, 0]]
					edges[cntedge, 1] = [nodes[i, 1], nodes[j, 1]]
					edgerecord[cntedge] = [i, j]
					cntedge+=1
					edgelim[i]+=1
					edgelim[j]+=1
				elif edgelim[j] < edgeLim(j) :
					continue
				else :
					break

# set edges in the dijkstra graph
for i in range(0, cntedge) :
	if edgerecord[i][0] % 20 == 0 and edgerecord[i][1] % 20 == 0 :
		plt.plot(edges[i, 0], edges[i, 1], color = "red")
	elif edgerecord[i][0] % 20 == 0 and edgerecord[i][1] % 5 == 0 :
		plt.plot(edges[i, 0], edges[i, 1], color = "green")
	elif edgerecord[i][0] % 20 == 0 :
		plt.plot(edges[i, 0], edges[i, 1], color = "blue")
	elif edgerecord[i][0] % 5 == 0 and edgerecord[i][1] % 5 == 0 :
		plt.plot(edges[i, 0], edges[i, 1], color = "orange")
	elif edgerecord[i][0] % 20 == 0 :
		plt.plot(edges[i, 0], edges[i, 1], color = "brown")
	else :
		plt.plot(edges[i, 0], edges[i, 1], color = "black")

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('dijkstra graph')
# showing legend
plt.legend()

# set limit for x and y axis
plt.xlim(0, 2000)
plt.ylim(0, 2000)

# function to show the plot
plt.show()

