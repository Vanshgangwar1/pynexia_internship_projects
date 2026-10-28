from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    # The queue stores tuples containing the current state and the path taken to get there
    # State is represented as (jug1_current, jug2_current)
    queue = deque([((0, 0), [(0, 0)])])
    
    # Set to keep track of visited states to prevent infinite loops
    visited = set()
    visited.add((0, 0))

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Goal check: If either jug has the target amount, return the path
        if jug1 == target or jug2 == target:
            return path

        # Generate all valid next states based on the pouring rules
        next_states = [
            (capacity1, jug2), # Rule 1: Fill Jug 1
            (jug1, capacity2), # Rule 2: Fill Jug 2
            (0, jug2),         # Rule 3: Empty Jug 1
            (jug1, 0),         # Rule 4: Empty Jug 2
            
            # Rule 5: Pour Jug 1 into Jug 2 
            # (Pour until Jug 1 is empty or Jug 2 is full)
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),
            
            # Rule 6: Pour Jug 2 into Jug 1 
            # (Pour until Jug 2 is empty or Jug 1 is full)
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))
        ]

        # Iterate through the generated states
        for state in next_states:
            if state not in visited:
                visited.add(state)
                # Append the new state and the updated path to the queue
                queue.append((state, path + [state]))

    # Return None if the queue empties and no solution is found
    return None

# Execution setup
if __name__ == "__main__":
    # Define fixed capacities and target quantity
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    # Run the search
    solution_path = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)

    # Display the exact sequence of state transitions
    if solution_path:
        print(f"Target of {target_amount} reached. Sequence of state transitions:")
        for step, state in enumerate(solution_path):
            print(f"Step {step}: Jug 1 = {state[0]}, Jug 2 = {state[1]}")
    else:
        print("No solution exists for the given capacities and target.")