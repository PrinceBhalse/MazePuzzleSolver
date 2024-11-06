from queue import PriorityQueue
from pyamaze import maze, agent

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs((x1 - x2) + (y1 - y2))

def aStar(m):
    # Initial position
    start = (m.rows, m.cols)
    g_cost = {cell: float('inf') for cell in m.grid}
    g_cost[start] = 0
    f_cost = {cell: float('inf') for cell in m.grid}
    f_cost[start] = h(start, (1, 1))

    # Storing values in Priority Queue
    open = PriorityQueue()  
    open.put((h(start, (1, 1)), start))  
    aPath = {}

    while not open.empty():
        currCell = open.get()[1]  # Extract cell from the tuple (priority, cell)
        if currCell == (1, 1):
            break
        for d in 'ESNW':  # East, South, North, West
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)

                temp_g_cost = g_cost[currCell] + 1
                temp_f_cost = temp_g_cost + h(childCell, (1, 1))

                if temp_f_cost < f_cost[childCell]:
                    g_cost[childCell] = temp_g_cost
                    f_cost[childCell] = temp_f_cost
                    open.put((temp_f_cost, childCell))  
                    aPath[childCell] = currCell

    # Reconstruct the path from (1,1) to start
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    
    return fwdPath

# Maze setup
m = maze(5, 5)
m.CreateMaze()

# Pathfinding and agent setup
path = aStar(m)
a = agent(m, footprints=True)
m.tracePath({a: path})

# Run the maze
m.run()
