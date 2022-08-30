# Installation (Uncomment the Line Below)
#!pip install gurobipy

# Import package
import gurobipy as op

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
x = prob.addVar(vtype=op.GRB.INTEGER, lb=0 , name='x')
y = prob.addVar(vtype=op.GRB.CONTINUOUS, lb=0, name='y')

# Add objective function to the environment
prob.setObjective(2*x+5*y, op.GRB.MAXIMIZE)

# Add constraints to the environment
prob.addConstr(5*x+3*y<=10, "const1")
prob.addConstr(2*x+7*y<=9, "const2")

# The status of the solution
prob.optimize()

# To display optimal decision variables
for v in prob.getVars():
    print('%s: %g' % (v.VarName, v.X))

# To display optimal value of objective function
print('Optimal Value of Objective Is =  %g' % prob.ObjVal)
