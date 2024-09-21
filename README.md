Name: Manan Arora
UTA ID: 1002143328
Programming Language used: Python

Code Structure:
    - a class expense_8_puzzle that contains all the functions excluding the main function
        - class contains functions as:
            - read_state = this function will read the state from the input file
            - find_blank = finding zero (blank place)
            - valid_moves = checking the valid moves from that particular position in puzzle
            - move = applies a move to the puzzle state and returns the new state
            - bfs = Breadth First Search Implementation
            - ucs = Uniform Cost Search Implementation
            - dfs = Depth First Search Implementation
            - dls = Depth Limited Search Implementation
            - ids = Iterative Depth Search Implementation
            - greedy = Greedy Search Implementation
            - a_star = A* Search Implementation
    - main function: takes the input from command line invocation with the format as: expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>
    and has all the input validations as mentioned in problem statement

How to Run the code:

    - python expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>
        - methods: bfs, ucs, dfs, dls, ids, greedy, a*
            - by default: a*
        - dump-flag: true, false
            - by default: false

