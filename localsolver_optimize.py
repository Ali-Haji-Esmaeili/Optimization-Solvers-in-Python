# Installation (Uncomment the Line Below) (Requires its software to be installed)
# !pip install localsolver -i https://pip.localsolver.com

# Import package
import localsolver

with localsolver.LocalSolver() as op:

    # Define environment
    prob = op.model

    # Define decision variables
    x = prob.int(0, None)
    y = prob.float(0, None)

    # Add constraints to the environment
    prob.constraint(5*x+3*y<=10)
    prob.constraint(2*x+7*y<=9)

    # Add objective function to the environment
    prob.maximize(2*x+5*y)
    
    # To display optimal decision variables
    prob.close()
    op.solve()
