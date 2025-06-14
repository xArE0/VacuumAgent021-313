## Avishek Shrestha 
# CRN: 021-313
# Date: 2025-06-14
# Q. Implementation of vacuum cleaning agent as a utility-based agent
# A. Calculates a utility score for every possible adjacent move.
# A. Dirty tiles get +100 points, and visited tiles get penalties (so it avoids looping).
# A. Picks the move with the highest score.

import random
import os
import time

# Parameters
WIDTH = 6
HEIGHT = 6
DIRT_PROBABILITY = 0.3
DELAY = 0.3

# Initialize room with random dirt
room = []
for i in range(WIDTH):
    row = []
    for j in range(HEIGHT):
        row.append(1 if random.random() < DIRT_PROBABILITY else 0)
    room.append(row)

# Agent's starting position
agent_x = random.randint(0, WIDTH - 1)
agent_y = random.randint(0, HEIGHT - 1)

# Directions (like king)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

# Memory for utility-based scoring
visited_count = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
path = [(agent_x, agent_y)]
step_count = 0

# Display
def print_room():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(WIDTH):
        row_str = ''
        for j in range(HEIGHT):
            if i == agent_x and j == agent_y:
                row_str += ' * '
            elif room[i][j] == 1:
                row_str += ' D '
            else:
                row_str += ' . '
        print(row_str)
    print()

# Goal test
def goal_reached():
    return all(1 not in row for row in room)

# Utility function
def calculate_utility(x, y):
    # Higher utility for dirty tiles and less visited ones
    utility = 0
    if room[x][y] == 1:
        utility += 100  # prioritize cleaning
    utility -= visited_count[x][y] * 5  # discourage repeating
    return utility

# Main loop
while not goal_reached():
    prev_x, prev_y = agent_x, agent_y

    # Clean if dirty
    if room[agent_x][agent_y] == 1:
        room[agent_x][agent_y] = 0

    visited_count[agent_x][agent_y] += 1

    print_room()
    print(f"Moved: ({prev_x}, {prev_y}) -> ({agent_x}, {agent_y})")
    time.sleep(DELAY)

    # Evaluate utility of all valid moves
    best_move = (agent_x, agent_y)
    best_utility = float('-inf')

    for dx, dy in directions:
        nx = agent_x + dx
        ny = agent_y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            utility = calculate_utility(nx, ny)
            if utility > best_utility:
                best_utility = utility
                best_move = (nx, ny)

    agent_x, agent_y = best_move
    path.append((agent_x, agent_y))
    step_count += 1

# Final output
print_room()
print("Cleaning complete.")
print(f"\nTotal steps taken: {step_count}")
print("Agent path:")
print(' -> '.join([f"({x},{y})" for x, y in path]))
