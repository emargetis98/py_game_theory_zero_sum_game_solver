# py_game_theory_zero_sum_game_solver
Python 3.12.5 source code for the function of calculating the equilibrium of a zero-sum game with LP.
In a zero-sum game, the gain of one player is exactly balanced by the loss of the other player.
The objective of the program is to find optimal mixed strategies for both players using the maximin strategy computation technique. To achieve this, the problem is modeled as a linear programming problem and solved using the optimization tools provided by the SCIP library. SCIP and its Python interface, pyscipopt, are libraries designed for solving mixed-integer programming problems and are used here to model the constraints and the objective function of the linear program.
The input instance is the matrix A, which defines the zero-sum game with payoff matrices R=A for the row player and C=-A for the column player, respectively. Variables are defined for the payoffs r and c, as well as for the mixed strategies x_vars and y_vars. The matrices R and C are specifically represented as two-dimensional NumPy arrays of shape (m,n).
To store the mixed strategies, the data structure np.array() is used, which facilitates matrix multiplication, element-wise operations, and probability validation. The class from pyscipopt used in this program is Model, which allows one to define variables, constraints, and the objective function.
The function quicksum is used to express summations in constraints and the objective function. The objective function/goal is to minimize the sum of the payoffs r+c, which represents the total gain for the players. In practice, this seeks to drive the sum of the payoffs to zero, which aligns with solving a zero-sum game, hence the use of minimization.
The constraints are based on the Mangasarian-Stone formulation for bimatrix zero-sum games, which ensures an optimal strategy for each player, given the mixed strategy of their opponent. It also guarantees that the mixed strategies of both players are probability vectors (i.e., non-negative vectors whose components sum to 1) over their respective action sets.
The practical interpretation is that the player must choose one of their actions with a certain probability, such that the sum of these probabilities equals 1. The constraints are added to the model using the command model.addCons().
Finally, the described model is optimized using SCIP, which handles the constraints and the objective function to determine the optimal mixed strategies.
For further info, look at 
1] T. Achterberg, «SCIP: Solving Constraint Integer Programs,» Mathematical Programming Computation. 
2] T. Achterberg, T. Berthold, T. Koch, and K. Wolter, «Constraint Integer Programming: a New Approach to
Integrate CP and MIP,» Integration of AI and OR Techniques in Constraint Programming for Combinatorial
Optimization Problems. 
