import sys

from timeit import default_timer as timer
from a_star import a_star_search

def main(arg):
    initial_state = []
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with open(arg, "r") as file:
        line = file.readline()
        for val in line.split(","):
            initial_state.append(int(val))

    if set(goal) != set(initial_state):
        sys.exit("ERROR: input is not valid, it must have numbers from 0 to 8")
    elif len(goal) != len(initial_state):
        sys.exit("ERROR: invalid input, it must have nine numbers, from 0 to 8")
    
    start = timer()
    final_state, explored_set, size = a_star_search(initial_state, goal)
    end = timer()
    
    if final_state != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(final_state.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(explored_set))
        print("=" * 20)
        print("Running time: %f sec" % (end - start))
        print("=" * 20)
        print("Bytes per node: %d" % sys.getsizeof(final_state))
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