import sys
import math

def generate_possible_moves(num_red, num_blue, mode):
    moves = []
    
    if num_red <= 0 or num_blue <= 0:
        print("Red and blue balls count must not be 0 or lower than 0.")
        return
        
    if mode == "standard":
        if num_red > 1:
            moves.append({"red": num_red - 2, "blue": num_blue, 'selected_color': "red"})
        if num_blue > 1:
            moves.append({"red": num_red, "blue": num_blue - 2, 'selected_color': "blue"})
        moves.append({"red": num_red - 1, "blue": num_blue, 'selected_color': "red"})
        moves.append({"red": num_red, "blue": num_blue - 1, 'selected_color': "blue"})

    elif mode == "misere":
        moves.append({"red": num_red, "blue": num_blue - 1, 'selected_color': "blue"})
        moves.append({"red": num_red - 1, "blue": num_blue, 'selected_color': "red"})
        if num_blue > 1:
            moves.append({"red": num_red, "blue": num_blue - 2, 'selected_color': "blue"})
        if num_red > 1:
            moves.append({"red": num_red - 2, "blue": num_blue, 'selected_color': "red"})

    return moves

def minimax_algorithm(current_state, depth_level, alpha_val, beta_val, is_maximizing, game_mode):
    if depth_level == 0 or current_state["blue"] == 0 or current_state["red"] == 0:
        score = -2 * current_state["red"] - 3 * current_state["blue"] if (game_mode == "standard" and is_maximizing) or (game_mode == "misere" and not is_maximizing) else 2 * current_state["red"] + 3 * current_state["blue"]
        return score
    
    if not is_maximizing:
        min_eval = math.inf
        for move in generate_possible_moves(current_state["red"], current_state["blue"], game_mode):
            score = minimax_algorithm(move, depth_level - 1, alpha_val, beta_val, True, game_mode)
            min_eval = min(min_eval, score)
            beta_val = min(beta_val, score)
            if min_eval <= alpha_val:
                break
        return min_eval

    else:
        max_eval = -math.inf
        for move in generate_possible_moves(current_state["red"], current_state["blue"], game_mode):
            score = minimax_algorithm(move, depth_level - 1, alpha_val, beta_val, False, game_mode)
            max_eval = max(max_eval, score)
            alpha_val = max(alpha_val, max_eval)
            if max_eval >= beta_val:
                break
        return max_eval

def determine_best_move(num_red, num_blue, mode, depth):
    optimal_score = -math.inf

    # before assignment
    best_color = None
    ball_count = 0

    possible_moves = generate_possible_moves(num_red, num_blue, mode)

    for move in possible_moves:
        move_score = minimax_algorithm(move, depth, -math.inf, math.inf, False, mode)
        if move_score > optimal_score:
            optimal_score = move_score
            best_color = move['selected_color']
            ball_count = (num_red - move["red"]) if move['selected_color'] == "red" else (num_blue - move["blue"])

    return best_color, ball_count

def start_game(num_red, num_blue, mode, current_player, max_depth):
    while True:
        if (num_red == 0 or num_blue == 0):
            if (current_player == "human"):
                if (mode == "standard"):
                    winner = "computer"
                else:
                    winner = "human"
            else:
                if(mode == "standard"):
                    winner = "human"
                else:
                    winner = "computer"

            print(f"\n{winner} wins with a score of:",((2 * num_red) + (3 * num_blue)), "\n")
            return

        color, num_balls = "", 0
        if current_player == "computer":
            color, num_balls = determine_best_move(num_red, num_blue, mode, max_depth)
            print(f"Computer picked: {num_balls} of {color} balls.")

        else:
            while True:
                color = input("Red / Blue").lower()
                if color not in ["red", "blue"]:
                    print(f"Please select a color from 'red' or 'blue'")
                else:
                    break

            if (color == "red"):
                total_available = num_red
            else:
                total_available = num_blue

            while True:
                print(f"Total Available balls are {total_available} for {color} color.")
                num_balls = int(input("Please provide number of balls you want to pick from (1 or 2)"))
                if (num_balls == 1 or num_balls == 2):
                    if (num_balls <= total_available):
                        break
                    else:
                        print(f"Number of balls selected, {num_balls} is greater than balls available for {color} that is {total_available}.")
                else:
                    print(f"Invalid input: {num_balls}. Please select either 1 or 2.")

        if color == "red":
            num_red -= num_balls
        else:
            num_blue -= num_balls

        print("Available:", num_red, "red balls,", num_blue, "blue balls")

        # swap turns
        if (current_player == "human"):
            current_player = "computer"
        else:
            current_player = "human"

def main():
    arguments = sys.argv

    # arguments less than 3
    if len(arguments) < 3:
        print("Incorrect Usage. Please follow correct usage: red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>")
        sys.exit(1)

    
    # Red Balls
    if int(arguments[1]) < 0:
        print("Number of Red Balls cannot be non-negative")
        sys.exit(1)
    else:
        num_red = int(arguments[1])

    # Blue Balls
    if int(arguments[2]) < 0:
        print("Number of Blue Balls cannot be non-negative")
        sys.exit(1) 
    else:
        num_blue = int(arguments[2])
    
    # Game version
    if len(arguments) > 3:
        if arguments[3].lower() not in ["standard", "misere"]:
            print("Please choose between 'standard' or 'misere'.")
            sys.exit(1)
        else:
            game_version = arguments[3].lower()
    else:
        game_version = "standard"
    
    # First player
    if len(arguments) > 4:
        if arguments[4].lower() not in ["computer", "human"]:
            print("Please choose between 'computer' or 'human'.")
            sys.exit(1)
        else:
            first_player = arguments[4].lower()
    else:
        first_player = "computer"

    # Depth
    if len(arguments) > 5:
        if int(arguments[5]) < -1:
            print("Depth must be an integer greater than or equal to -1.")
            sys.exit(1)
        else:
            depth = int(arguments[5])
    else:
        depth = -1

    print("\nInitial setup for the game: \n")
    print(f"Red balls count = {num_red}")
    print(f"Blue balls count = {num_blue}")
    print(f"Game version = {game_version}")
    print(f"First player move = {first_player}")
    print(f"Depth = {depth}")

    start_game(num_red, num_blue, game_version, first_player, depth)

if __name__ == "__main__":
    main()