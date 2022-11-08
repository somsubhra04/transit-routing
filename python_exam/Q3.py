"""
Enter the solution for Q3 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import numpy as np
def number_of_routes(source_stopid: str, destination_stopid: str) -> int:
    """
    Find the number of routes going from source stop id to destination stop id.

    Args:
        source_stopid (str): Source Stop Id
        destination_stopid (str): Destination Stop Id

    Returns:
        final_count (int): Number of routes going from source to destination.
    """
    final_count = -1
    try:
        # Enter your code here
        with open(__file__[:-5] + "stop_times.txt") as f:
            linect = f.readlines()
        for i in range(len(linect)):
            linect[i] = linect[i][:-1].split(',')[:4]
        
        linect = linect[1:]

        trip_to_stops = {}
        for i in range(len(linect)):
            trip_to_stops[linect[i][0]] = [ ]
    
        for i in range(len(linect)):
            trip_to_stops[linect[i][0]].append(linect[i][1])

        with open(__file__[:-5] + "trips.txt") as f:
            linect = f.readlines()
        
        for i in range(len(linect)):
            linect[i] = linect[i][:-1].split(',')[:2]
        linect = linect[1:]
        return final_count
    except:
        return final_count
