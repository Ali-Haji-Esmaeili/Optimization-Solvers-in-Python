# Installation (Uncomment the Line Below)
#!pip install cplex 
#!pip install docplex

# Import package
import docplex as op

# Define environment
prob = op.mp.model.Model("MyOptProblem")

# Define decision variables
x = prob.integer_var(lb=0,ub=None)
y = prob.continuous_var(lb=0,ub=None)

# Add objective function to the environment
prob.set_objective("max", 2*x+5*y)

# Add constraints to the environment
prob.add_constraint(5*x+3*y<=10, ctname="const1")
prob.add_constraint(2*x+7*y<=9, ctname="const2")

# The status of the solution
prob.print_information()
prob.solve()

# To display optimal decision variables
prob.print_solution()

# To display optimal value of objective function
print("Optimal Value of Objective Is = ",prob.objective_value)
