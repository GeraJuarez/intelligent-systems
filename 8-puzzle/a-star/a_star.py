import sys
import queue

from node import Node
from state import State

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

def manhattan_priority(state):
    """Calculates the Manhattan priority according to the positions of the puzzle numbers

    Return the Manhattan distance from each current number position to that of the goal
    """
    priority = 0
    for i, val in enumerate(state):
        if (val == 0): continue
        row_dist = abs(ROW_VALS[i] - ROW_VALS[val])
        col_dist = abs(COL_VALS[i] - COL_VALS[val])
        priority += row_dist + col_dist

    return priority

def a_star_search(initial_state, final_state):
    """Search based on heuristic, in this case, with the Manhattan priority function"""

    # Init variables
    heap_state = queue.PriorityQueue()
    explored = set()
    size_bytes_counter = 0

    # Inner helper function
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

        print("Depth %d" % len(state_current.path))
        print(*heap_state.queue, sep='\n')
            
    return None, None, None