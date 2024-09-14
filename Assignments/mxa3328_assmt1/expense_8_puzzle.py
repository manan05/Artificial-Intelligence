# this is a modified version of the 8 puzzle problem implemented by Manan Arora (mxa3328)

import heapq
import sys
from collections import deque
import math


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
        # if zero is in 1st row or 2nd, row 0 can move UP but the other tile moves DOWN
        if (x > 0):
            moves.append((x-1, y, "down"))

        # if zero is in 0th row or 1st row it can move DOWN but the other tile moves UP
        if (x < 2):
            moves.append((x + 1, y, "up"))

        # if zero is in 1st column or 2nd column it can move LEFT but the other tile moves RIGHT
        if (y > 0):
            moves.append((x, y - 1, "right"))

        # if zero is in 0th column or 1st column it can move RIGHT but the other tile moves LEFT
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
        visited.add(tuple(tuple(row) for row in start_state))

        if(dump_flag):
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Queue initially: {queue} \n")
                dump_file.write(f"Visited Set: {visited} \n")

        nodes_popped = 0
        nodes_expanded = 0
        nodes_generated = 0
        max_fringe_size = 0

        if(dump_flag):
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Nodes Popped Initially: {nodes_popped} \n")
                dump_file.write(f"Nodes Expanded Initially: {nodes_expanded} \n")
                dump_file.write(f"Nodes Generated Initially: {nodes_generated} \n")
                dump_file.write(f"Max Fringe Size Initially: {max_fringe_size} \n")

        while queue:
            if(dump_flag):
                with open('trace_dump.txt', 'a') as dump_file:
                    dump_file.write(f"Queue: {queue} \n")

            max_fringe_size = max(max_fringe_size, len(queue))
            current_state, path, total_cost = queue.popleft()
            nodes_popped += 1
            if(dump_flag):
                with open('trace_dump.txt', 'a') as dump_file:
                    dump_file.write(f"Nodes Popped : {nodes_popped} \n")
                    dump_file.write(f"Nodes Expanded : {nodes_expanded} \n")
                    dump_file.write(f"Nodes Generated : {nodes_generated} \n")
                    dump_file.write(f"Max Fringe Size : {max_fringe_size} \n")

            # Check if the current state matches the goal state
            if current_state == goal_state:
                if(dump_flag):
                    with open('trace_dump.txt', 'a') as dump_file:
                        dump_file.write("Solution Found!")
                        dump_file.write(f"Current State: {current_state} \n")
                        dump_file.write(f"Goal State: {goal_state} \n")
                        dump_file.write(f"Nodes Popped Initially: {nodes_popped} \n")
                        dump_file.write(f"Nodes Expanded Initially: {nodes_expanded} \n")
                        dump_file.write(f"Nodes Generated Initially: {nodes_generated} \n")
                        dump_file.write(f"Max Fringe Size Initially: {max_fringe_size} \n")
                        dump_file.write(f"Solution found at depth: {len(path)} with cost of {total_cost} \n")

                print("Nodes Popped: ", nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Nodes Generated: ", nodes_generated)
                print("Max Fringe Size: ", max_fringe_size)
                print(
                    f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    if(dump_flag):
                        with open('trace_dump.txt', 'a') as dump_file:
                            dump_file.write(f"Move {i[0]} {i[1]} \n")
                    print(f"Move {i[0]} {i[1]}")
                return
            
            # if the current state not goal state that means it should be expanded

            nodes_expanded += 1

            if(dump_flag):
                with open('trace_dump.txt', 'a') as dump_file:
                    dump_file.write(f"Nodes Popped : {nodes_popped} \n")
                    dump_file.write(f"Nodes Expanded : {nodes_expanded} \n")
                    dump_file.write(f"Nodes Generated : {nodes_generated} \n")
                    dump_file.write(f"Max Fringe Size : {max_fringe_size} \n")

            # Explore valid moves
            for new_move in self.valid_moves(puzzle=current_state):
                if(dump_flag):
                    with open('trace_dump.txt', 'a') as dump_file:
                        dump_file.write(f"New Moved from Current State: {new_move} \n")

                new_state, direction, cost = self.move(
                    puzzle=current_state, move=new_move)
                
                if(dump_flag):
                    with open('trace_dump.txt', 'a') as dump_file:
                        dump_file.write(f"New State: {new_state} \n")
                        dump_file.write(f"Direction: {direction} \n")
                        dump_file.write(f"Cost: {cost} \n")
                
                state_tuple = tuple(tuple(row) for row in new_state)

                if(dump_flag):
                    with open('trace_dump.txt', 'a') as dump_file:
                        dump_file.write(f"State Tuple: {state_tuple} \n")

                # If the new state hasn't been visited yet
                if (state_tuple not in visited):
                    if(dump_flag):
                        with open('trace_dump.txt', 'a') as dump_file:
                            dump_file.write(f"State Tuple: {state_tuple} \n")
                            dump_file.write(f"Visited: {visited} \n")
                            dump_file.write(f"Size of Visited: {len(visited)} \n")
                            dump_file.write(f"State Tuple is not in visited \n")
                    
                    visited.add(state_tuple)

                    if(dump_flag):
                        with open('trace_dump.txt', 'a') as dump_file:
                            dump_file.write(f"Added the state to visited \n")
                            dump_file.write(f"Visited Now: {visited} \n")
                            dump_file.write(f"Size of Visited: {len(visited)} \n")

                    queue.append(
                        (new_state, path + [(cost, direction)], total_cost + cost))
                    nodes_generated += 1

                    if(dump_flag):
                        with open('trace_dump.txt', 'a') as dump_file:
                            dump_file.write(f"Queue now: {queue} \n")
                            dump_file.write(f"Incrementing nodes_generated: {nodes_generated} \n")

        if(dump_flag):
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"No Solution found! \n")
        print("No solution found.")


    # TODO: DUMP FILE 
    def ucs(self, start_state_file, goal_state_file, dump_flag):
        # Uniform Cost Search implementation
        
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        priority_queue = []
        heapq.heappush(priority_queue, (0, start_state, []))  # (total_cost, current_state, path)

        visited = set()
        visited.add(tuple(tuple(row) for row in start_state))

        nodes_popped = 0
        nodes_expanded = 0
        nodes_generated = 0
        max_fringe_size = 0

        while priority_queue:
            max_fringe_size = max(max_fringe_size, len(priority_queue))

            total_cost, current_state, path = heapq.heappop(priority_queue)
            nodes_popped += 1

            if current_state == goal_state:
                print(f"Nodes Popped: {nodes_popped}")
                print(f"Nodes Expanded: {nodes_expanded}")
                print(f"Nodes Generated: {nodes_generated}")
                print(f"Max Fringe Size: {max_fringe_size}")
                print(f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for move in path:
                    print(f"Move {move[0]} {move[1]}")
                return
            
            nodes_expanded += 1

            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(row) for row in new_state)

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    heapq.heappush(priority_queue, (total_cost + cost, new_state, path + [(cost, direction)]))
                    nodes_generated += 1

        print("No solution found.")

    # TODO: DUMP FILE
    def dfs(self, start_state_file, goal_state_file, dump_flag):
        # depth first search implementation
        
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        stack = [(start_state, [], 0)]  # [(current_state, path, total cost)]

        visited = set()
        for i in start_state:
            visited.add(tuple(tuple(i)))

        nodes_popped = 0
        nodes_generated = 0
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
                print("Nodes Generated: ", nodes_generated)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(
                    f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return

            nodes_expanded += 1

            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(i) for i in new_state)

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    stack.append((new_state, path + [(cost, direction)], total_cost + cost))
                    nodes_generated += 1
        
        print("No solution found.")

    # TODO: Dump flag implementation
    def dls(self, start_state_file, goal_state_file, dump_flag):
        # depth limited search implementation

        depth_limit = int(input("Enter the depth limit for DLS: "))
        print(f"DLS implementation with depth limit: {depth_limit}")
    
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        stack = [(start_state, [], 0, 0)]  # [(current_state, path, total cost, current_depth)]

        visited = set()
        for i in start_state:
            visited.add(tuple(tuple(i)))

        nodes_popped = 0
        nodes_generated = 0
        nodes_expanded = 0
        max_fringe_size = 0

        while stack:
            max_fringe_size = max(max_fringe_size, len(stack))
            current_state, path, total_cost, current_depth = stack.pop()
            nodes_popped += 1

            # If we reach the goal state
            if current_state == goal_state:
                print("Nodes Popped: ", nodes_popped)
                print("Nodes Generated: ", nodes_generated)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return

            # Skip expanding if the depth limit has been reached
            if current_depth >= depth_limit:
                continue

            nodes_expanded += 1

            # Expand the current state
            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(i) for i in new_state)

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    stack.append((new_state, path + [(cost, direction)], total_cost + cost, current_depth + 1))
                    nodes_generated += 1

        print("No solution found within the depth limit.")

    # TODO: Dump flag implementation
    def ids(self, start_state_file, goal_state_file, dump_flag):
        # Iterative Deepening search implementation
        depth_limit = 0

        while True:
            print(f"Searching with depth limit: {depth_limit}")
            
            # Perform depth-limited search with the current depth limit
            start_state = self.read_state(start_state_file)
            goal_state = self.read_state(goal_state_file)

            stack = [(start_state, [], 0, 0)]  # [(current_state, path, total cost, current_depth)]
            visited = set()
            for i in start_state:
                visited.add(tuple(tuple(i)))

            nodes_popped = 0
            nodes_generated = 0
            nodes_expanded = 0
            max_fringe_size = 0
            solution_found = False

            while stack:
                max_fringe_size = max(max_fringe_size, len(stack))
                current_state, path, total_cost, current_depth = stack.pop()
                nodes_popped += 1

                # If we reach the goal state
                if current_state == goal_state:
                    print("Nodes Popped: ", nodes_popped)
                    print("Nodes Generated: ", nodes_generated)
                    print("Nodes Expanded: ", nodes_expanded)
                    print("Max Fringe Size: ", max_fringe_size)
                    print(f"Solution found at depth: {len(path)} with cost of {total_cost}")
                    print("Steps: ")
                    for i in path:
                        print(f"Move {i[0]} {i[1]}")
                    solution_found = True
                    break  # Exit the while loop

                # Skip expanding if the depth limit has been reached
                if current_depth >= depth_limit:
                    continue

                nodes_expanded += 1

                # Expand the current state
                for new_move in self.valid_moves(puzzle=current_state):
                    new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                    state_tuple = tuple(tuple(i) for i in new_state)

                    if state_tuple not in visited:
                        visited.add(state_tuple)
                        stack.append((new_state, path + [(cost, direction)], total_cost + cost, current_depth + 1))
                        nodes_generated += 1

            if solution_found:
                return  # Solution found, exit the function

            # Increment the depth limit and try again

            print(f"No solution found at depth limit: {depth_limit}")
            print("Incrementing depth limit \n")
            depth_limit += 1


    def greedy(self, start_state_file, goal_state_file, dump_flag):
        # greedy search implementation
        start_state = self.read_state(start_state_file)
        goal_state = self.read_state(goal_state_file)

        # Heuristic Function: Manhattan
        def heuristic(current_state, goal_state):
            distance = 0
            for i in range(3):
                for j in range(3):
                    if current_state[i][j] != 0:  # Skip the blank tile
                        goal_position = [(row, col) for row in range(3) for col in range(3) if goal_state[row][col] == current_state[i][j]][0]
                        distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)
            return distance
        
        # Heuristic function: Euclidean
        def euc(current_state,goal_state):
            distance = 0
            for i in range(3):
                for j in range(3):
                    if current_state[i][j] != 0:  # Skip the blank tile
                        goal_position = [(row, col) for row in range(3) for col in range(3) if goal_state[row][col] == current_state[i][j]][0]
                        distance += math.sqrt((goal_position[0] - i)**2 + (goal_position[1] - j)**2)
            return distance
        
        # Priority queue (min-heap), initialized with the start state and its heuristic
        pq = []
        heapq.heappush(pq, (heuristic(start_state, goal_state), start_state, [], 0))  # (heuristic, current_state, path, total_cost)
        
        visited = set()
        for i in start_state:
            visited.add(tuple(tuple(i)))
        
        nodes_popped = 0
        nodes_generated = 0
        nodes_expanded = 0
        max_fringe_size = 0
        
        while pq:
            max_fringe_size = max(max_fringe_size, len(pq))
            
            # Get the state with the lowest heuristic value
            heuristic_value, current_state, path, total_cost = heapq.heappop(pq)
            nodes_popped += 1
            
            if current_state == goal_state:
                print("Nodes Popped: ", nodes_popped)
                print("Nodes Generated: ", nodes_generated)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Fringe Size: ", max_fringe_size)
                print(f"Solution found at depth: {len(path)} with cost of {total_cost}")
                print("Steps: ")
                for i in path:
                    print(f"Move {i[0]} {i[1]}")
                return
            
            nodes_expanded += 1
            
            # Generate valid moves from the current state
            for new_move in self.valid_moves(puzzle=current_state):
                new_state, direction, cost = self.move(puzzle=current_state, move=new_move)
                state_tuple = tuple(tuple(i) for i in new_state)
                
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    # Add to priority queue based on the heuristic value of the new state
                    new_heuristic = heuristic(new_state, goal_state)
                    heapq.heappush(pq, (new_heuristic, new_state, path + [(cost, direction)], total_cost + cost))
                    nodes_generated += 1
        
        print("No solution found.")



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

    if dump_flag:
        with open('trace_dump.txt', 'a') as dump_file:
            dump_file.write(f"Command Line Arguments: [{start_state}, {goal_state}, {method}, 'true'] \n")

    if method == "bfs":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.bfs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
        
    elif method == "ucs":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.ucs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "dfs":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.dfs(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "dls":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.dls(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "ids":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.ids(start_state_file=start_state,
                     goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "greedy":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.greedy(start_state_file=start_state,
                        goal_state_file=goal_state, dump_flag=dump_flag)
    elif method == "a*":
        if dump_flag:
            with open('trace_dump.txt', 'a') as dump_file:
                dump_file.write(f"Method selected: {method} \n")
                dump_file.write(f"Implementing  {method} \n")

        solution.a_star(start_state_file=start_state,
                        goal_state_file=goal_state, dump_flag=dump_flag)
    else:
        print("Please check the inputs arguments and try again...")
        return


if __name__ == "__main__":
    main()
