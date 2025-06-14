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
DELAY = 0.5

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

# Memory
visited = set()
path = [(agent_x, agent_y)]
step_count = 0

# Directions (like king in chess)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

# Display function
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

# Main loop
while not goal_reached():
    prev_x, prev_y = agent_x, agent_y
    visited.add((agent_x, agent_y))

    # Clean if dirty
    if room[agent_x][agent_y] == 1:
        room[agent_x][agent_y] = 0

    print_room()
    print(f"Moved: ({prev_x}, {prev_y}) -> ({agent_x}, {agent_y})")
    time.sleep(DELAY)

    # Priority 1: move to adjacent dirty tile
    moved = False
    for dx, dy in directions:
        nx = agent_x + dx
        ny = agent_y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if room[nx][ny] == 1:
                agent_x, agent_y = nx, ny
                moved = True
                break

    # Priority 2: move to unvisited tile
    if not moved:
        unvisited_moves = []
        for dx, dy in directions:
            nx = agent_x + dx
            ny = agent_y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if (nx, ny) not in visited:
                    unvisited_moves.append((nx, ny))
        if unvisited_moves:
            agent_x, agent_y = random.choice(unvisited_moves)
            moved = True

    # Priority 3: fallback to random adjacent move
    if not moved:
        random.shuffle(directions)
        for dx, dy in directions:
            nx = agent_x + dx
            ny = agent_y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                agent_x, agent_y = nx, ny
                break

    path.append((agent_x, agent_y))
    step_count += 1

# Final state and summary
print_room()
print("Cleaning complete.")
print(f"\nTotal steps taken: {step_count}")
print("Agent path:")
print(' -> '.join([f"({x},{y})" for x, y in path]))
