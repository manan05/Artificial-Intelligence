# this is a modified version of the 8 puzzle problem implemented by Manan Arora (mxa3328)

import sys


class expense_8_puzzle:
    def readState(state_file):
        puzzle = []
        with open(state_file, 'r') as file:
            for i in file:
                print(i)

    def bfs(start_state, goal_state, dump_flag):
        # Breadth First Search implementation
        
        print("bfs implementation")
        pass

    def ucs(start_state, goal_state, dump_flag):
        # uniform cost search implementation
        
        print("ucs implementation")
        pass

    def dfs(start_state, goal_state, dump_flag):
        # depth first search implementation

        print("dfs implementation")
        pass

    def dls(start_state, goal_state, dump_flag):
        # depth limited search implementation

        print("dls implementation")
        pass

    def ids(start_state, goal_state, dump_flag):
        # Iterative Deepening search implementation

        print("ids implementation")
        pass

    def greedy(start_state, goal_state, dump_flag):
        # greedy search implementation

        print("greedy implementation")
        pass

    def a_star(start_state, goal_state, dump_flag):
        # A* search implementation

        print("A* implementation")
        pass

    def main():
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
            if (arguments[3] == 'True' or arguments[3] == 'true') :
                method = "a*"
                dump_flag = True
            elif(arguments[3] == 'False' or arguments[3] == 'false'):
                method = "a*"
                dump_flag = False
            else:
                method = arguments[3]
                dump_flag = False      
        else:
            method = arguments[3]
            if (arguments[4] == 'True' or arguments[4] == 'true'):
                dump_flag = True
            else:
                dump_flag = False

        print("start_state: ", start_state)
        print("goal_state: ", goal_state)
        print("method: ", method)
        print("dump_flag: ", dump_flag)

        if(method == "bfs"):
            expense_8_puzzle.bfs(start_state, goal_state, dump_flag)
        elif(method == "ucs"):
            expense_8_puzzle.ucs(start_state, goal_state, dump_flag)
        elif(method == "dfs"):
            expense_8_puzzle.dfs(start_state, goal_state, dump_flag)
        elif(method == "dls"):
            expense_8_puzzle.dls(start_state, goal_state, dump_flag)
        elif(method == "ids"):
            expense_8_puzzle.ids(start_state, goal_state, dump_flag)
        elif(method == "greedy"):
            expense_8_puzzle.greedy(start_state, goal_state, dump_flag)
        elif(method == "a*"):
            expense_8_puzzle.a_star(start_state, goal_state, dump_flag)
        else:
            print("Please check the inputs arguments and try again...")
            return

if __name__ == "__main__":
    expense_8_puzzle.main()
