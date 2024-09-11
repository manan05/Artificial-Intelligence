# # this is a modified version of the 8 puzzle problem implemented by Manan Arora (mxa3328)

import heapq
from math import cos
import sys
from collections import deque
from tracemalloc import start

from IPython import start_kernel


class expense_8_puzzle:
    # this function will read the state from the input file and returns a 2D representation of the state
    def read_state(self, state_file):
        puzzle = []
        with open(state_file, "r") as file:
            for i in file:
                i.strip()
                if (i == "END OF FILE"):
                    break
                puzzle.append([int(num) for num in i.split()])
        return puzzle

    # finding zero (empty place)
    def find_zero(self, puzzle):
        for i in range(3):
            for j in range(3):
                if (puzzle[i][j] == 0):
                    return i, j

    # checking the valid moves from that particular position in puzzle
    def valid_moves(self, puzzle):
        moves = []

        x, y = self.find_zero(puzzle=puzzle)
        # if zero is in 1st row or 2nd row it can move UP but not if it is in 0th row
        if (x > 0):
            moves.append((x-1, y, "down"))

        # if zero is in 0th row or 1st row it can move DOWN but not if it is in 2nd row
        if (x < 2):
            moves.append((x + 1, y, "up"))

        # if zero is in 1st column or 2nd column it can move LEFT but not if it is in 0th column
        if (y > 0):
            moves.append((x, y - 1, "right"))

        # if zero is in 0th column or 1st column it can move RIGHT but not if it is in 2nd column
        if (y < 2):
            moves.append((x, y + 1, "left"))

        return moves

    # applies a move to the puzzle state and returns the new state
    def move(self, puzzle, move):
        x, y = self.find_zero(puzzle=puzzle)
        after_move_puzzle = [row[:] for row in puzzle]
        new_x, new_y, direction = move

        tile_moved = after_move_puzzle[new_x][new_y]
        after_move_puzzle[x][y], after_move_puzzle[new_x][new_y] = after_move_puzzle[new_x][new_y], after_move_puzzle[x][y]

        return after_move_puzzle, direction, tile_moved

    def bfs(self, start_state_file, goal_state_file, dump_flag):
        # Breadth First Search implementation

        # Reading the start and goal state of the puzzle
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        queue = deque([(start_state, [], 0)]) # (current_state, path, total cost)

        visited = set()  # To store visited states
        for i in start_state:
            visited.add(tuple(tuple(i)))

        nodes_popped = 0
        nodes_expanded = 0
        max_fringe_size = 0

        while queue:
            max_fringe_size = max(max_fringe_size, len(queue))
            current_state, path, total_cost = queue.popleft()
            nodes_popped += 1

            # Check if the current state matches the goal state
            if current_state == goal_state:
                print("Nodes Popped: ", nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(
                    f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return

            # Explore valid moves
            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(
                    puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(row) for row in new_state)

                # If the new state hasn't been visited yet
                if (state_tuple not in visited):
                    visited.add(state_tuple)
                    queue.append(
                        (new_state, path + [(cost, direction)], total_cost + cost))
                    nodes_expanded += 1

        print("No solution found.")

    def ucs(self, start_state_file, goal_state_file, dump_flag):
        # uniform cost search implementation
        print("ucs implementation")

        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        priority_queue = []
        heapq.heappush(priority_queue, (0, start_state, []))

        visited = set()
        for i in start_state:
            visited.add(tuple(tuple(i)))

        nodes_popped = 0
        nodes_expanded = 0
        max_fringe_size = 0

        while (priority_queue):
            max_fringe_size = max(max_fringe_size, len(priority_queue))

            total_cost, current_state, path = heapq.heappop(priority_queue)
            nodes_popped += 1

            if (current_state == goal_state):
                print("Nodes Popped: ", nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(
                    f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return

            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(
                    puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(row) for row in new_state)

                if (state_tuple not in visited):
                    visited.add(state_tuple)
                    heapq.heappush(priority_queue, (total_cost +
                                   cost, new_state, path + [(cost, direction)]))
                    nodes_expanded += 1

        print("No solution found.")

    def dfs(self, start_state_file, goal_state_file, dump_flag):
        # depth first search implementation
        print("dfs implementation")
        
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        stack = [(start_state, [], 0)]  # [(current_state, path, total cost)]

        visited = set()
        for i in start_state:
            visited.add(tuple(tuple(i)))

        nodes_popped = 0
        nodes_expanded = 0
        max_fringe_size = 0
        i = 0
        while stack:
            print(i)
            i += 1
            max_fringe_size = max(max_fringe_size, len(stack))
            current_state, path, total_cost = stack.pop()
            nodes_popped += 1

            if(current_state == goal_state):
                print("Nodes Popped: ", nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(
                    f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return
            
            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(i) for i in new_state)

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    stack.append((new_state, path + [(cost, direction)], total_cost + cost))
                    nodes_expanded += 1
        
        print("No solution found.")

    def dls(self, start_state_file, goal_state_file, dump_flag):
        # depth limited search implementation

        print("dls implementation")
        pass

    def ids(self, start_state_file, goal_state_file, dump_flag):
        # Iterative Deepening search implementation

        print("ids implementation")
        pass

    def greedy(self, start_state_file, goal_state_file, dump_flag):
        # greedy search implementation

        print("greedy implementation")
        pass

    def a_star(self, start_state_file, goal_state_file, dump_flag):
        # A* search implementation

        print("A* implementation")
        pass


def main():
    solution = expense_8_puzzle()
    arguments = sys.argv
    if len(arguments) < 3 or len(arguments) > 5:
        print("Please check the input command and try again")
        return
    start_state = arguments[1]
    goal_state = arguments[2]
    if len(arguments) == 3:
        # No Argument other than Start and goal state
        # Default method and dump_flag
        method = "a*"
        dump_flag = False

    elif len(arguments) == 4:
        if arguments[3] == "True" or arguments[3] == "true":
            method = "a*"
            dump_flag = True
        elif arguments[3] == "False" or arguments[3] == "false":
            method = "a*"
            dump_flag = False
        else:
            method = arguments[3]
            dump_flag = False
    else:
        method = arguments[3]
        if arguments[4] == "True" or arguments[4] == "true":
            dump_flag = True
        else:
            dump_flag = False

    # print("start_state: ", start_state)
    # print("goal_state: ", goal_state)
    # print("method: ", method)
    # print("dump_flag: ", dump_flag)

    if method == "bfs":
        solution.bfs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "ucs":
        solution.ucs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "dfs":
        solution.dfs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "dls":
        solution.dls(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "ids":
        solution.ids(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "greedy":
        solution.greedy(start_state_file=start_state,
                        goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "a*":
        solution.a_star(start_state_file=start_state,
                        goal_state_file=goal_state, dump_flag=dump_flag)
    else:
        print("Please check the inputs arguments and try again...")
        return


if __name__ == "__main__":
    main()
