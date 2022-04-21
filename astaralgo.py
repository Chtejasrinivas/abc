def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node) 
        closed_set = set()
        g = {}
        parents = {}
 
        g[start_node] = 0
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None
 
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                         
     
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                            
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
 
 
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
        H_dist = {
            'S': 5,
            'A': 5,
            'B': 3,
            'C': 4,
            'D': 6,
            'E': 5,
            'F': 6,
            'G1': 0,
            'G2': 0,
            'G3': 0,
             
        }
 
        return H_dist[n]
 
Graph_nodes = {
    'S': [('A', 5), ('B', 9),('D', 6)],
    'A': [('B', 3),('G1', 9)],
    'B': [('A', 2),('C', 1)],
    'C': [('S', 6), ('G2', 5),('F', 7)],
    'D': [('C', 2), ('E', 2),('S', 1)],
    'E': [('G3', 7)],
    'F': [('D', 2),('G3', 8)],

     
}
aStarAlgo('S', 'G2')