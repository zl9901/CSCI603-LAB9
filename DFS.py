graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def DFS(graph,s):
    stack=[]
    stack.append(s)
    seen=set()
    seen.add(s)
    parent = {s: None}
    while len(stack)>0:
        vertex=stack.pop()
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
                parent[w]=vertex
        print(vertex)
    return parent



def test():
    # print(graph.keys())
    # print(graph.values())
    # print(graph["A"])

    parent=DFS(graph,"A")
    hp = "F"
    arr = []
    while hp is not None:
        arr.append(hp)
        hp = parent[hp]
    print(arr)

if __name__ == '__main__':
    test()