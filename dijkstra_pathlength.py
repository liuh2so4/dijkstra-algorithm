import random
import math
def edgeLim(x) :
    if x % 20 == 0 :
        return 10
    elif x % 5 == 0 :
        return 5
    else :
        return 3

def distance(x, y, z, w) :
    return math.sqrt((x-z)*(x-z) + (y-w)*(y-w))

data = 10000
boarder = 20000

nodes = {}
for i in range(0, 10) :
    # set random nodes
    for i in range(0, data) :
        for j in range(0, 2) :
            nodes[i, j] = random.randint(0, boarder)
    me_link_SD = {}
    for i in range(0, data) :
      for j in range(0, 10) :
          me_link_SD[i, j] = [0, 0]
    edgelim = {}
    for i in range(0, data) :
       edgelim[i] = 0
    # set edges with rules
    for i in range(0, data) :
        if i % 20 == 0 :
           for j in range(i+1, data) :
              if (j % 20 == 0 and distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/2) or (j % 5 == 0 and distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/4) or distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/8 :
                    if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
                        me_link_SD[i, edgelim[i]] = [j, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[i]+=1
                        me_link_SD[j, edgelim[j]] = [i, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[j]+=1
                    elif edgelim[j] < edgeLim(j) :
                        continue
                    else :
                        break
        elif i % 5 == 0 :
            for j in range(i+1, data) :
                if j % 5 == 0 and distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/2 or distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/4 :
                    if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
                        me_link_SD[i, edgelim[i]] = [j, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[i]+=1
                        me_link_SD[j, edgelim[j]] = [i, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[j]+=1
                    elif edgelim[j] < edgeLim(j) :
                        continue
                    else :
                        break
        else :
            for j in range(i+1, data) :
                if distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1]) <= boarder/3 :
                    if edgelim[i] < edgeLim(i) and edgelim[j] < edgeLim(j) :
                        me_link_SD[i, edgelim[i]] = [j, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[i]+=1
                        me_link_SD[j, edgelim[j]] = [i, distance(nodes[i, 0], nodes[i, 1], nodes[j, 0], nodes[j, 1])]
                        edgelim[j]+=1
                    elif edgelim[j] < edgeLim(j) :
                        continue
                    else :
                        break
    sum = 0
    edgesum = 0
    for i in range(0, data):
        for j in range(0, edgelim[i]):
            sum += me_link_SD[i, j][1]
            edgesum += 1
    avg = sum / edgesum
    print(avg)
