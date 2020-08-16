graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph,s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    parent={s:None}
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w]=vertex
        print(vertex)
    return parent







def test():
    # print(graph.keys())
    # print(graph.values())
    # print(graph["A"])
    parent= BFS(graph,"E")
    for key in parent:
        print(key,parent[key])

    hp="B"
    arr = []
    while hp is not None:
        arr.append(hp)
        hp = parent[hp]
    print(arr)



if __name__ == '__main__':
    test()