# # this is a modified version of the 8 puzzle problem implemented by Manan Arora (mxa3328)

import sys
from collections import deque


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

    def valid_moves(self, puzzle):
        moves = []

        # finding zero (empty place)
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if (puzzle[i][j] == 0):
                    x, y = i, j

        # if zero is in 1st row or 2nd row it can move UP but not if it is in 0th row
        if (x > 0):
            moves.append((x-1, y, "up"))

        # if zero is in 0th row or 1st row it can move DOWN but not if it is in 2nd row
        if (x < 2):
            moves.append((x + 1, y, "down"))

        # if zero is in 1st column or 2nd column it can move LEFT but not if it is in 0th column
        if (y > 0):
            moves.append((x, y - 1, "left"))

        # if zero is in 0th column or 1st column it can move RIGHT but not if it is in 2nd column
        if (y < 2):
            moves.append((x, y + 1, "right"))
            
        return moves

    def bfs(self, start_state, goal_state, dump_flag):
        # Breadth First Search implementation
        start_puzzle = self.read_state(start_state)
        end_puzzle = self.read_state(goal_state)

        print(self.valid_moves(start_puzzle))

        # print("bfs implementation")
        print("start_puzzle", start_puzzle)
        # print("end_puzzle", end_puzzle)

    def ucs(self, start_state, goal_state, dump_flag):
        # uniform cost search implementation

        print("ucs implementation")
        pass

    def dfs(self, start_state, goal_state, dump_flag):
        # depth first search implementation

        print("dfs implementation")
        pass

    def dls(self, start_state, goal_state, dump_flag):
        # depth limited search implementation

        print("dls implementation")
        pass

    def ids(self, start_state, goal_state, dump_flag):
        # Iterative Deepening search implementation

        print("ids implementation")
        pass

    def greedy(self, start_state, goal_state, dump_flag):
        # greedy search implementation

        print("greedy implementation")
        pass

    def a_star(self, start_state, goal_state, dump_flag):
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

    print("start_state: ", start_state)
    print("goal_state: ", goal_state)
    print("method: ", method)
    print("dump_flag: ", dump_flag)

    if method == "bfs":
        solution.bfs(start_state, goal_state, dump_flag)
    elif method == "ucs":
        solution.ucs(start_state, goal_state, dump_flag)
    elif method == "dfs":
        solution.dfs(start_state, goal_state, dump_flag)
    elif method == "dls":
        solution.dls(start_state, goal_state, dump_flag)
    elif method == "ids":
        solution.ids(start_state, goal_state, dump_flag)
    elif method == "greedy":
        solution.greedy(start_state, goal_state, dump_flag)
    elif method == "a*":
        solution.a_star(start_state, goal_state, dump_flag)
    else:
        print("Please check the inputs arguments and try again...")
        return


if __name__ == "__main__":
    main()
