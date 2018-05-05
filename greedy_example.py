def basic_greedy():
    # greedy search algorithm
    d_dict = {1: [(1, 2), (2, 15), (3, 30)], 2: [(1, 30), (7, 10)]}  # dict of lists of tuples such that nodei : [ (neighbourj, distancej), .... ]
    currentCity = 1
    tour = []   # list of covered nodes
    tour.append(currentCity)
    distanceTravelled = 0   # distance travelled in tour
    while len(set([neighbourCity for (neighbourCity, distance) in d_dict.get(currentCity, [])]).difference(set(tour))) > 0:  # set(currentCityNeighbours) - set(visitedNodes)
        # way 1 starts
        minDistanceNeighbour = None
        minDistance = None
        for eachNeighbour, eachNeighbourdDistance in d_dict[currentCity]:
            if eachNeighbour != currentCity and eachNeighbour not in tour:
                if minDistance is not None:
                    if minDistance > eachNeighbourdDistance:
                        minDistance = eachNeighbourdDistance
                        minDistanceNeighbour = eachNeighbour
                else:
                    minDistance = eachNeighbourdDistance
                    minDistanceNeighbour = eachNeighbour
        nearestNeigbhourCity = (minDistanceNeighbour, minDistance)
        # way 1 ends
        # way 2 starts
        # nearestNeigbhourCity = min(d_dict[currentCity], key=lambda someList: someList[1] if someList[0] not in tour else 1000000000)  # else part returns some very large number
        # way 2 ends
        tour.append(nearestNeigbhourCity[0])
        currentCity = nearestNeigbhourCity[0]
        distanceTravelled += nearestNeigbhourCity[1]
    print(tour)
    print(distanceTravelled)