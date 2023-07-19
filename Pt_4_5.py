def findpath(GRaf, start_point, end_point, path):
    path = path + [start_point]
    paths = []
    if start_point == end_point:
        return [path]
    if start_point not in GRaf:
        return []
    for current in GRaf[start_point]:
        new_paths = findpath(GRaf, current, end_point, path)
        paths += new_paths
    return paths


paths = []
GRaf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'

print(findpath(GRaf, start, end, paths))
