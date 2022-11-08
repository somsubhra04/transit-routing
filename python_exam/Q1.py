"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import numpy as np
# defining the Dij_generator function
def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        with open(r"C:\Users\Somsubhra\transit-routing\python_exam\ChicagoSketch_net.tntp") as f:
        linect = f.readlines()
        linect = linect[9:]
        init = []
        length = []
        termct = []
        for i in range(len(linect)):
            tval = linect[i].split()
            init.append(int(tval[0]))
            termct.append(int(tval[1]))
            length.append(float(tval[4]))
        
        v1 = max(init)
        v2 = max(termct)
        graph_object = np.ones((v1, v2))*np.inf

        for i in range(len(length)):
            graph_object[init[i]-1][termct[i]-1] = length[i]
        return graph_object
    except:
        return graph_object

def mini_dist(dist, dist_cal):
    mn = np.inf
    for i in range(dist.shape[0]):
        if dist_cal[i]==0 and dist[i]<mn:
            mn = dist[i]
            mini_index = i
    return mini_index

def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        # Enter your code here
        V = graph_object.shape[1]
        dist = np.ones(V) * np.inf
        dist[source-1] = 0
        dist_cal = np.zeros(V)
        
        for i in range(V):
            u = mini_dist(dist, dist_cal)
            dist_cal[u] = 1
            for v in range(V):
                is_neighbour = graph_object[u][v]!=np.inf
                if (is_neighbour):
                    new_dist = dist[u] + graph_object[u][v]
                    if(dist[v] > new_dist):
                        dist[v] = new_dist
        shortest_path_distance = dist[destination-1] if dist[destination-1]!= np.inf else -1
        return shortest_path_distance
    except:
        return shortest_path_distance
graph_object = Dij_generator() #graph_object: tuple to store mult values
print(Q1_dijkstra(139, 305, graph_object))
