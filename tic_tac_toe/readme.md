# Unbeatable Tic-Tac-Toe AI (Minimax Algorithm)

A Python implementation of Tic-Tac-Toe where a human player competes against an AI powered by the **Minimax Algorithm**. The AI evaluates every possible future move to ensure it plays optimally, guaranteeing it never loses.

---

##  Features

- **Optimal Decision Making:** Uses full depth-first minimax search tree exploration.
- **Depth-Weighted Scoring:** Prioritizes faster victories and delays potential losses.
- **Validation Engine:** Real-time state detection for invalid moves, wins, losses, and draws.
- **Interactive CLI:** Clear 3x3 grid display updated after every turn.

---

##  How Minimax Works

Minimax is a recursive backtracking decision rule algorithm used in two-player zero-sum games.

- **Maximizer (AI - `O`):** Tries to achieve the highest possible score ($+10$).
- **Minimizer (Human - `X`):** Tries to force the lowest possible score ($-10$).

### Decision Tree Evaluation

The recursive utility value $V(s)$ for a state $s$ is defined as:

$$V(s) = \begin{cases} +10 - \text{depth} & \text{if AI wins} \\ -10 + \text{depth} & \text{if Human wins} \\ 0 & \text{if Draw} \\ \max_{a \in A} V(\text{Result}(s, a)) & \text{if AI turn} \\ \min_{a \in A} V(\text{Result}(s, a)) & \text{if Human turn} \end{cases}$$

---

##  Requirements & Execution

### Prerequisites
- Python 3.x (No external packages required).

### Run the Game
```bash
python tic_tac_toe.py