import heapq
import math
graph = {
    "A": {"B":5,"C":1},
    "B": {"A":5, "C":2, "D":1},
    "C": {"A":1, "B":2, "D":4, "E":8},
    "D": {"B":1, "C":4, "E":3, "F":6},
    "E": {"C":8, "D":3},
    "F": {"D":6}
}


def init_distance(graph,s):
    """
     distance中存放的都是各个节点到点A的距离
     """
    distance = {s: 0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex]=math.inf
    return distance

def dijkstra(graph,s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))
    """
    相当于将一对数据存于优先队列中
    """
    seen=set()
    seen.add(s)
    parent={s:None}
    distance=init_distance(graph,s)
    while len(pqueue)>0:
        pair=heapq.heappop(pqueue)
        """
        记住dist为到优先队列刚刚pop出的点到出发点的距离
        """
        dist=pair[0]
        vertex=pair[1]
        seen.add(vertex)
        nodes=graph[vertex].keys()
        print(nodes)
        for w in nodes:
            if w not in seen:
                if dist+graph[vertex][w]<distance[w]:
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    """
                    优先队列中的数字代表，该数字前的节点到A节点的距离
                    """
                    parent[w]=vertex
                    distance[w]=dist+graph[vertex][w]
        print(vertex)
    return parent,distance






def test():
    # print(graph.keys() )
    # print(graph.values())
    # print(graph["A"])
    parent,distance= dijkstra(graph,"A")
    print(parent)
    print(distance)

if __name__ == '__main__':
    test()