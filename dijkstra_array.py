import random
import math
import time
def edgeLim(x) :
    if x % 20 == 0 :
        return 10
    elif x % 5 == 0 :
        return 5
    else :
        return 3

def distance(x, y, z, w) :
    return math.sqrt((x-z)*(x-z) + (y-w)*(y-w))

data = 20000
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
    sec = time.time()
    termination = 0
    pre_dist = {}
    pre_dist[0] = [data + 1, 0, 0]
    for i in range(1, data) :
        pre_dist[i] = [-1, -1, -1]
    for i in range(0, edgelim[0]) :
        pre_dist[me_link_SD[0, i][0]] = [0, me_link_SD[0, i][1], me_link_SD[0, i][0]]
    def findmin(array) :
        minn = 0
        mindist = boarder * 10
        for i in range(1, data) :
            if array[i][0] >= 0 and array[i][0] < data  and array[i][1] < mindist :
                mindist = array[i][1]
                minn = array[i][2]
        return minn
    cnt = 0
    while cnt < data :
        minnode = findmin(pre_dist)
        # print(cnt, minnode)
        if(minnode ==  data - 1) :
            termination = pre_dist[minnode][1]
            # break
        for i in range(0, edgelim[minnode]) :
            if pre_dist[me_link_SD[minnode, i][0]][1] < 0 :
                pre_dist[me_link_SD[minnode, i][0]] = [minnode, pre_dist[minnode][1] + me_link_SD[minnode, i][1], me_link_SD[minnode, i][0]]
            elif pre_dist[me_link_SD[minnode, i][0]][1] > pre_dist[minnode][1] + me_link_SD[minnode, i][1] :
                pre_dist[me_link_SD[minnode, i][0]] = [minnode, pre_dist[minnode][1] + me_link_SD[minnode, i][1], me_link_SD[minnode, i][0]]
        cnt += 1
        pre_dist[minnode] = [data + 1, 0, minnode]   
    # for i in range(0, data) :
        # print(i, pre_dist[i])
    # if pre_dist[data - 1][1] < 0 :
        # print("Invalid graph! There's no way to exceed the termination")
    # else :
        # print("The shortest path length is", termination)
    sec = time.time() - sec
    print(sec)
