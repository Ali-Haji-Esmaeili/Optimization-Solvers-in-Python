# Installation (Uncomment the Line Below)
#!pip install xpress

# Import package
import xpress as op

# Define decision variables
x = op.var(vartype=op.integer)
y = op.var()
z = 2 * x + 5 * y

# Define environment
prob = op.problem("MyOptProb")
prob.addVariable(x)
prob.addVariable(y)

# Add constraints to the environment
prob.addConstraint(5*x+3*y <= 10)
prob.addConstraint(2*x+7*y <= 9)

# Add objective function to the environment
prob.setObjective(z, sense=op.maximize)

# The status of the solution
prob.solve()

# To display optimal decision variables
print("x: ", prob.getSolution(x))
print("y: ",prob.getSolution(y))

# To display optimal value of objective function
print("Optimal Value of Objective Is = ", prob.getSolution(z))
