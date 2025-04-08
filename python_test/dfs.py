def dfs(graph, start, visited=None):
    """
    深度优先搜索递归实现
    :param graph: 用邻接表表示的图（字典类型）
    :param start: 起始节点
    :param visited: 已访问集合（递归时自动传递）
    :return: 深度优先遍历顺序列表
    """
    if visited is None:
        visited = set()
    traversal_order = []

    if start not in visited:
        traversal_order.append(start)
        visited.add(start)
        # 递归访问相邻节点（注意这里使用sorted保证可重复性）
        for neighbor in sorted(graph[start]):
            traversal_order += dfs(graph, neighbor, visited)

    return traversal_order


# 示例图的邻接表表示
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]  # 自循环
}

# 测试DFS
start_node = 2
print(f"从节点 {start_node} 开始的DFS遍历顺序：")
print(dfs(graph, start_node))  # 输出: [2, 0, 1, 3]