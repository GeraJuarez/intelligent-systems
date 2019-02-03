import sys
import queue

from timeit import default_timer as timer

from node import Node
from state import State

def a_start(initial_state, final_state):
    """Search based on heuristic, i thos case, with the Manhattan priority function"""

    # Init variables
    heap_state = queue.PriorityQueue()
    explored = set()
    size_bytes_counter = 0

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

    # Inner helper functions
    def manhattan_priority(state):
        priority = 0
        for i, val in enumerate(state):
            if (val == 0): continue
            row_dist = abs(ROW_VALS[i] - ROW_VALS[val])
            col_dist = abs(COL_VALS[i] - COL_VALS[val])
            priority += row_dist + col_dist

        return priority

    def explore_next(neighbor_puzzle, move_type):
        """Finds out if the neighbor_puzzle is within the boundaries and explore it.
        `explored` is the set of States already visited.
        `heap_state` is the heap that keeps States to be visited sorted by priority.
        `state_current` the current State that is being visited.
        """
        if (neighbor_puzzle != None and tuple(neighbor_puzzle) not in explored):
            state_next = State(neighbor_puzzle)
            state_next.path = state_current.path.copy()
            state_next.path.append(move_type)
            state_next.f_heuristic = manhattan_priority(state_next.puzzle) + len(state_next.path)
            heap_state.put(state_next)

    # Start algorithm
    state_first = State(initial_state)
    state_first.f_heuristic = manhattan_priority(state_first.puzzle)
    heap_state.put(state_first)

    while not heap_state.full():
        state_current = heap_state.get()
        size_bytes_counter += sys.getsizeof(state_current)

        # Add an unmodified list to the set, a tuple
        explored.add(tuple(state_current.puzzle))

        if final_state == state_current.puzzle:
            return state_current, explored, size_bytes_counter
        
        # Create a node of the current state
        node_current = Node(state_current.puzzle)

        # Iterate over posible paths
        explore_next(*node_current.up())
        explore_next(*node_current.down())
        explore_next(*node_current.left())
        explore_next(*node_current.right())
            
    return None, None, None

def main(arg):
    initial_state = []
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with open(arg, "r") as file:
        line = file.readline()
        for val in line.split(" "):
            initial_state.append(int(val))

    if set(goal) != set(initial_state):
        sys.exit("ERROR: input is not valid, it must have numbers from 0 to 8")
    elif len(goal) != len(initial_state):
        sys.exit("ERROR: invalid input, it must have nine numbers, from 0 to 8")
    
    start = timer()
    final_state, explored_set, size = a_start(initial_state, goal)
    end = timer()
    
    if final_state != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(final_state.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(explored_set))
        print("=" * 20)
        print("Running time: %f sec" % (end - start))
        print("=" * 20)
        print("Bytes per node: %d" % sys.getsizeof(State(goal)))
        print("Used memory: %d bytes" % size)
        print("=" * 20)
        print("This are the movements to solve the puzzle:")
        print("-" * 20)
        print(*final_state.path, sep=' => ')
    else:
        print("It has no solution :(")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("ERROR: The program needs the name of the file with the initial state of the puzzle as an argument when executing")
    elif len(sys.argv) > 2:
        sys.exit("ERROR: too many arguments")

    main(sys.argv[1])