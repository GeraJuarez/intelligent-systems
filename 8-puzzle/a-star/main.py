import sys
import heapq

from timeit import default_timer as timer

from node import Node
from state import State

def a_start(initialState, finalState):
    """Search based on heuristic, i thos case, with the Manhattan priority function"""

    # Init variables
    stateHeap = []
    explored = set()
    sizeBytesCounter = 0

    # Constants dictionaries for distnces inside the puzzle pieces
    ROW_VALS = {
        0:0, 1:1, 2:2,
        3:0, 4:1, 5:2,
        6:0, 7:1, 8:2
    }

    COL_VALS = {
        0:0, 1:0, 2:0,
        3:1, 4:1, 5:1,
        6:2, 7:2, 8:2
    }

    def calculateManhattan(state):
        priority = 0
        for i, val in enumerate(state.puzzle):
            rowDist = abs(ROW_VALS[i] - ROW_VALS[val])
            colDist = abs(COL_VALS[i] - COL_VALS[val])
            priority += rowDist + colDist

        return priority

    def exploreNext(neighbor_state, move_type):
        """Finds out if the neighbor_state is within the boundaries and explore it.
        `explored` is the set used in the BFS function.
        `stateQueue` is the queue inside the BFS function.
        `currentState` is each visited node inside the loop of the BFS function.

        """
        if (neighbor_state != None and tuple(neighbor_state) not in explored):
            nextState = State(neighbor_state)
            nextState.path = currentState.path.copy()
            nextState.path.append(move_type)
            stateQueue.append(nextState)

    # Init heap
    first = State(initialState))
    tupState = (calculateManhattan(first), tupState)
    heappush(stateHeap, tupState)

    # while heap is not empty
    while stateHeap:
        currentState = heappop(stateHeap)
        sizeBytesCounter += sys.getsizeof(currentState)

        # Add an unmodified list to the set, a tuple
        explored.add(tuple(currentState.puzzle))

        if finalState == currentState.puzzle:
            return currentState, explored, sizeBytesCounter
        
        # Create a node of the current state
        currentNode = Node(currentState.puzzle)

        # Iterate over posible paths
        exploreNext(*currentNode.up())
        exploreNext(*currentNode.down())
        exploreNext(*currentNode.left())
        exploreNext(*currentNode.right())
            
    return None, None, None

def main(arg):
    initialState = []
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with open(arg, "r") as file:
        line = file.readline()
        for val in line.split(" "):
            initialState.append(int(val))

    if set(goal) != set(initialState):
        sys.exit("ERROR: input is not valid, it must have numbers from 0 to 8")
    elif len(goal) != len(initialState):
        sys.exit("ERROR: invalid input, it must have nine numbers, from 0 to 8")
    
    start = timer()
    finalState, exploredSet, size = a_start(initialState, goal)
    end = timer()
    
    if finalState != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(finalState.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(exploredSet))
        print("=" * 20)
        print("Running time: %f sec" % (end - start))
        print("=" * 20)
        print("Bytes per node: %d" % sys.getsizeof(State(goal)))
        print("Used memory: %d bytes" % size)
        print("=" * 20)
        print("This are the movements to solve the puzzle:")
        print("-" * 20)
        print(*finalState.path, sep=' => ')
    else:
        print("It has no solution :(")

if len(sys.argv) < 2:
    sys.exit("ERROR: The program needs the name of the file with the initial state of the puzzle as an argument when executing")
elif len(sys.argv) > 2:
    sys.exit("ERROR: too many arguments")

main(sys.argv[1])