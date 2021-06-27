
import heapq

import sys

 

input = sys.stdin.readline

 

n, m = map(int, input().split())

INF = int(1e9)

 

distance = [INF]* (n+1)

graph = [[]* (n+2) for _ in range(n+2)]

 

for i in range(m):

    a, b = map(int,input().split())

    graph[a].append(b)

    graph[b].append(a)

 

q = []

distance[1] = 0

heapq.heappush(q,(0,1,0))

#d, start, total

 

while q:

    cd, cx, ct = heapq.heappop(q)

    

    if cx!=1 and distance[cx]<cd:

        continue

 

    for i in range((len(graph[cx]))):

        # print("graph",graph[cx][i])

        cost = 1+ cd

        if cost<distance[graph[cx][i]]:

            heapq.heappush(q,(cost,graph[cx][i],ct+1))

            distance[graph[cx][i]] = cost

 

# for i in range(n):

#     print(distance[i])

 

mx = 0

for i in range(n+1):

    if distance[i]!=INF and mx<distance[i]:

        mx = distance[i]

ct = 0

mx_idx = 0

for i in range(n+1):

    if mx == distance[i]:

        mx_idx =i

        break

for i in range(n+1):

    if mx ==distance[i]:

        ct+=1

print(mx_idx, mx, ct, end=" ")