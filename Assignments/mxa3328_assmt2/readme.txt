Name: Manan Arora
UTA ID: 1002143328

Programming Language used: Python 3.9.7

Code Structure:

    1. generate_possible_moves(num_red, num_blue, mode) = generates and returns all possible moves based on the counts of red and blue balls and the game mode(standard or misere)
    
    2. eval_function(current_state, is_maximizing, mode) = evaluates a game state and assigns a score based on the current player's maximizing or minimizing goal, adjusting by game mode
    
    3. minimax_algorithm(current_state, depth_level, alpha_val, beta_val, is_maximizing, mode) = a minimax algo with alpha-beta pruning to evaluate possible moves recursively, optimizing the computer's strategy
    
    4. best_move(num_red, num_blue, mode, depth) = it finds the computers optimal move by scoring each possible move using minimax_algorithm
    
    5. start_game(num_red, num_blue, mode, current_player, max_depth) = runs the main game loop, and alternates the turns between the computer and the human player until one wins
    
    6. main() = initializes game settings from command line arguments and begins the game with start_game function

How to Run the Code:
    Requirements: Python 3.9.7

    Command line execution: python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>
        <num-red> = number of red balls (must be non negative)
        <num-blue> = number of blue balls (must be non negative)
        <version> = game version (standard or misere). default is standard
        <first-player> = starting player (computer or human). default is computer
        <depth> = depth level for the minimax algorithm. Default is -1(unlimited depth).
         