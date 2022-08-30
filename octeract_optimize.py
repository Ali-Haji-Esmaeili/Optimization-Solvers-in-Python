# Installation (Please refer to its website) (Requires its software to be installed)

from octeract import *

#============================================================================#
#Ensure to credit the original developer:
#Platform: https://github.com/ktafakkori
#Repository: Optimization-Solvers-in-Python
#Developer: © Keivan Tafakkori 
#Year: 2022
#Month: August
#Day: 30
#Source: https://github.com/ktafakkori/Optimization-Solvers-in-Python
#============================================================================#

# Define environment
prob = Model("MyOptProblem")

# Define decision variables
prob.add_variable("x", 0, None, INT)
prob.add_variable("y", 0, None)

# Add objective function to the environment
prob.set_objective("2*x+5*y", MAXIMIZE)

# Add constraints to the environment
prob.add_constraint("5*x+3*y<=10")
prob.add_constraint("2*x+7*y<=9")

# To display optimal decision variables (using 4 threads)
prob.global_solve(4)
