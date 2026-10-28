# Water Jug Problem Solver

An optimal Python implementation of the classic **Water Jug Problem** using **Breadth-First Search (BFS)**. This solver models the state space of two ungraduated jugs and finds the shortest sequence of state transitions required to measure a target quantity of water.

---

Key Features

- **Guaranteed Shortest Path:** Uses Breadth-First Search (BFS) to explore the state space level-by-level, guaranteeing the minimal number of pouring steps.
- **Cycle Prevention:** Uses a Python `set` to track visited states, preventing infinite loops.
- **State Path Tracking:** Captures and displays the complete sequence of state transitions `(jug1_current, jug2_current)` from initial state `(0, 0)` to the final goal.

