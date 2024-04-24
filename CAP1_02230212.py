''' Deepa gurung
B.E ICE
02230212
References
Links that i have refered while solving :
https://www.w3schools.com/python/python_dictionaries.asp#:~:text=Dictionaries%20are%20used%20to%20store,and%20earlier%2c%20dictionaries%20are%20unordered.
https://youtu.be/_uQrJ0TkZlc?si=KPZF0V_UC8ED5StP
https://youtu.be/Qcefu1jVPds?si=yiLz18J8xNOWcNGA
and got help from software engineering friends
Solution'''
def read_input_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]

# Calculating the score for each rounds 
def calculate_round_score(player_choice, opponent_choice, outcome):
    choices = {'A': 1, 'B': 2, 'C': 3}
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}
    player_score = choices[player_choice] + outcomes[outcome]
    opponent_score = choices[opponent_choice] + outcomes[outcome]
    return player_score, opponent_score

# Determine the player's choice based on the outcome
def determine_player_choice(opponent_choice, outcome):
    if outcome == 'Y':
        return opponent_choice  # Draw, choose the same as the opponent
    elif outcome == 'X':
        return 'C' if opponent_choice == 'A' else 'A' if opponent_choice == 'B' else 'B'  # Lose
    else:
        return 'B' if opponent_choice == 'A' else 'C' if opponent_choice == 'B' else 'A'  # Win

# Calculate the total score
def calculate_total_score(rounds):
    total_score = 0
    for opponent_choice, outcome in rounds:
        player_choice = determine_player_choice(opponent_choice, outcome)
        player_score, _ = calculate_round_score(player_choice, opponent_choice, outcome)
        total_score += player_score
    return total_score

# File name for data
filename = "input_2_cap1.txt"  # Update according to the input file name

# Read input file
rounds = read_input_file(filename)

# Calculate the total score
total_score = calculate_total_score(rounds)

# Output total score
print("Total score:", total_score)