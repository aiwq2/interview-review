import sys

def dijkstra(graph, start):
    # 初始化距离字典，将起始节点的距离设为0，其他节点的距离设为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 初始化已访问节点的集合和未访问节点的集合
    visited = set()
    unvisited = set(graph)

    while unvisited:
        # 选择当前距离最小的节点
        current_node = min(unvisited, key=lambda node: distances[node])

        # 更新当前节点的邻居节点的距离
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

        # 将当前节点标记为已访问，并从未访问集合中移除
        visited.add(current_node)
        unvisited.remove(current_node)

    return distances

# 测试代码
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("最短路径：")
for node, distance in distances.items():
    print(f"从节点 {start_node} 到节点 {node} 的最短距离为 {distance}")
