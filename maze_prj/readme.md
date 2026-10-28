# Grid Maze Solver using A* Search Algorithm

An efficient Python solver that calculates and visualizes the shortest path through a 2D obstacle grid using the **A* Search Algorithm**.

---

## Features

- **Optimal Pathfinding:** Guarantees finding the shortest route from start to goal when an admissible heuristic is used.
- **Multiple Heuristics:** Supports both **Manhattan Distance** (optimal for 4-directional grid movement) and **Euclidean Distance**.
- **Obstacle Navigation:** Accurately routes around static wall barriers.
- **Unreachable Path Handling:** Gracefully handles unsolvable mazes where barriers completely block access to the destination.
- **ASCII Visualization:** Renders grid layout, start (`S`), goal (`G`), walls (`█`), and calculated path (`*`).

---

##  Mathematics of A* Search

A* balances actual path distance from the start node with an estimated heuristic distance to the goal node:

$$f(n) = g(n) + h(n)$$

Where:
- $g(n)$: Exact path cost from the start node to current node $n$.
- $h(n)$: Heuristic estimate of the remaining cost from node $n$ to the goal.
- $f(n)$: Total estimated cost of the cheapest solution path through node $n$.

### Heuristic Formulas

1. **Manhattan Distance** (4-directional movement):
   $$h(n) = \vert{}x_1 - x_2\vert{} + \vert{}y_1 - y_2\vert{}$$

2. **Euclidean Distance** (Straight-line distance):
   $$h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

---

##  Requirements & Execution

### Prerequisites
- Python 3.x (Uses standard modules `heapq` and `math`; no third-party package dependencies).

### Running the Solver
```bash
python maze_solver.py