import numpy as np
from pyscipopt import Model, quicksum

def solve_zero_sum_game(A):
    m, n = A.shape
    R = A  # Payoff matrix for the Row player
    C = -A # Payoff matrix for the Column player (since it's a zero-sum game)

    model = Model("ZeroSumGame")

    # Define variables
    r = model.addVar(name="r", lb=None)  # Payoff for the Row player
    c = model.addVar(name="c", lb=None)  # Payoff for the Column player
    x_vars = [model.addVar(name=f"x_{i}", lb=0) for i in range(m)]  # Mixed strategy for the Row player
    y_vars = [model.addVar(name=f"y_{j}", lb=0) for j in range(n)]  # Mixed strategy for the Column player

    # Objective: Minimize r + c
    model.setObjective(r + c, "minimize")

    # Constraints based on the Mangasarian-Stone formulation:
    # Row player constraints: r * 1 - R * y >= 0 for each row
    for i in range(m):
        model.addCons(
            r - quicksum(R[i, j] * y_vars[j] for j in range(n)) >= 0,
            name=f"row_constraint_{i}"
        )

    # Column player constraints: c * 1 - C^T * x >= 0 for each column
    for j in range(n):
        model.addCons(
            c - quicksum(C[i, j] * x_vars[i] for i in range(m)) >= 0,
            name=f"column_constraint_{j}"
        )

    # Probability constraint for the Row player's strategy: sum(x) = 1
    model.addCons(quicksum(x_vars) == 1, name="sum_x_eq_1")

    # Probability constraint for the Column player's strategy: sum(y) = 1
    model.addCons(quicksum(y_vars) == 1, name="sum_y_eq_1")

    # Hide SCIP Optimization Suite output details
    model.hideOutput()  

    # Solve the model
    model.optimize()

    # Check if the model found an optimal solution
    if model.getStatus() == "optimal":
        x = np.array([model.getVal(x_var) for x_var in x_vars])
        y = np.array([model.getVal(y_var) for y_var in y_vars])
        return x, y
    else:
        print("No optimal solution found. Status:", model.getStatus())
        return None, None
