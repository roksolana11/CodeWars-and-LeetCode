def tree_by_levels(node):
    if node is None:
        return []
    result = []
    queue = [node]
    while queue:
        i = queue.pop(0)
        result.append(i.value)
        if i.left:
            queue.append(i.left)

        if i.right:
            queue.append(i.right)
    return result
