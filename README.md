# Vacuum Cleaning Agents Labwork

**Student Name:** Avishek Shrestha  
**CRN:** 021-313  
**Date:** 2025-06-14

---

## Project Overview

This repository contains implementations of three types of vacuum cleaner agents in Python, designed to operate within a virtual room environment with randomly generated dirt:

- **Goal-Based Agent:** Uses memory and goal-testing to clean the environment efficiently.  
- **Simple Reflex Agent:** Acts based solely on the current state of the environment without memory.  
- **Utility-Based Agent:** Selects actions based on a utility function to balance cleaning and exploration.
  
Each agent navigates a 2D grid room, detects dirt, and cleans it by moving intelligently around the space.

---
## Goal-Based Agent

The Goal-Based Agent maintains memory of visited locations and uses a goal test to determine if cleaning is complete. It prioritizes moving towards dirty cells and keeps track of its path.

**Images:**  
- Initial Room State: ![Goal Based Initial State](https://github.com/user-attachments/assets/2d0af10f-c503-4923-bf4e-50b744a2a9ac)

- Final Output:![Goal Based Output](https://github.com/user-attachments/assets/6eb4d035-3649-4e71-86ff-e2c6978b3bec)
---
## Simple Reflex Agent

The Simple Reflex Agent acts only on the current cell's condition without memory. It cleans if the current spot is dirty and moves randomly otherwise, responding purely to immediate perceptions.

**Images:**  
- Initial Room State:![SimpleRefAgent Initial](https://github.com/user-attachments/assets/ae013b89-6938-44ca-8957-a744144c7149)
- Final Output: ![SimpleRefAgent Output](https://github.com/user-attachments/assets/d2c0011c-1aae-4d04-8491-7e5e811c12af)
---

## Utility-Based Agent

The Utility-Based Agent evaluates possible moves based on a utility function balancing dirt cleaning and exploration, aiming to maximize overall performance over time.

**Images:**  
- Initial Room State:![UtilityBased Initial](https://github.com/user-attachments/assets/9063d01e-5b12-4bb3-8d9b-314e3e83f750)
- Final Output:![UtilityBased Output](https://github.com/user-attachments/assets/6ad12c4c-50a3-4075-a6fd-28ccddb4ab6e)
---
