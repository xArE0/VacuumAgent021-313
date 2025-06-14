# Avishek Shrestha 
# CRN: 021-313
# Date: 2023-10-01
# Q. Implementation of vacuum cleaning agent as a goal based agent with memory

import random
import os
import time

# Parameters
WIDTH = 6
HEIGHT = 6
DIRT_PROBABILITY = 0.3
DELAY = 0.3

# Initializing room with random dirt
room = []
for i in range(WIDTH):
    row = []
    for j in range(HEIGHT):
        if random.random() < DIRT_PROBABILITY:
            row.append(1)
        else:
            row.append(0)
    room.append(row)

# Agent's starting position
agent_x = random.randint(0, WIDTH - 1)
agent_y = random.randint(0, HEIGHT - 1)

# Memory of visited cells
visited = set()

# Directions (8 directions around the agent)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

# Display each state
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
    for row in room:
        if 1 in row:
            return False
    return True

# Main loop
while not goal_reached():
    visited.add((agent_x, agent_y))

    # Clean if dirty
    if room[agent_x][agent_y] == 1:
        room[agent_x][agent_y] = 0

    print_room()
    time.sleep(DELAY)

    # Find next move
    possible_moves = []
    for dx, dy in directions:
        nx = agent_x + dx
        ny = agent_y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if room[nx][ny] == 1 or (nx, ny) not in visited:
                possible_moves.append((nx, ny))

    # Move to next best position
    if possible_moves:
        agent_x, agent_y = random.choice(possible_moves)
    else:
        # If stuck, just move randomly
        random.shuffle(directions)
        for dx, dy in directions:
            nx = agent_x + dx
            ny = agent_y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                agent_x, agent_y = nx, ny
                break

# Final room state
print_room()
print("Cleaning complete.")
