# remove mark work add
import heapq
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2, 4],
    4: [3, 5, 6],
    5: [4, 6],
    6: [4, 5]
}

weight = {
    (0, 1): 10,
    (0, 3): 40,
    (1, 0): 10,
    (1, 2): 10,
    (2, 1): 10,
    (2, 3): 10,
    (3, 0): 40,
    (3, 2): 10,
    (3, 4): 2,
    (4, 3): 2,
    (4, 5): 3,
    (4, 6): 8,
    (5, 4): 3,
    (5, 6): 3,
    (6, 4): 8,
    (6, 5): 3
}

seen = set()

q = [(0, None, 0)]

while q:
    cost, par, node = heapq.heappop(q)
    if node in seen:
        continue
    if par is not None:
        print("From: ", node, " To: ", par, " Cost: ", cost)

    seen.add(node)

    for nei in graph[node]:
        if nei not in seen:
            heapq.heappush(q, (weight[(node, nei)], node, nei))

# Another Graph
print("\n")

graph = {
    1: [2, 3],
    2: [5],
    3: [2, 4],
    4: [5],
    5: []
}

weight = {
    (1, 2): 4,
    (1, 3): 1,
    (3, 2): 2,
    (3, 4): 4,
    (2, 5): 4,
    (4, 5): 4
}

seen = set()

q = [(0, None, 1)]

while q:
    cost, par, node = heapq.heappop(q)
    if node in seen:
        continue
    if par is not None:
        print("From: ", node, " To: ", par, " Cost: ", cost)

    seen.add(node)

    for nei in graph[node]:
        if nei not in seen:
            heapq.heappush(q, (weight[(node, nei)], node, nei))
