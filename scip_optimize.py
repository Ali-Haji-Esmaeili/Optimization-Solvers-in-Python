# Installation (Requires msvc>=14.0 for building binaries from its source code) (Uncomment the Line Below)
# !pip install pyscipopt 

# Import package
import pyscipopt as op

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
prob = op.Model("MyOptProblem")  

# Define decision variables
x = prob.addVar("x", vtype="INTEGER")
y = prob.addVar("y")

# Add objective function to the environment
prob.setObjective(2*x+5*y,  sense='maximize')

# Add constraints to the environment
prob.addCons(5*x+3*y<=10)
prob.addCons(2*x+7*y<=9)

# The status of the solution
prob.optimize()

# To display optimal decision variables
sol = prob.getBestSol()
print("x: {}".format(sol[x]))
print("y: {}".format(sol[y]))

# To display optimal value of objective function
print("Optimal Value of Objective Is = ", prob.getObjective())
