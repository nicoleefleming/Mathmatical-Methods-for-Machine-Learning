# Title     : Use Linear Programming to solve for the Primal and Dual Programs presented in 7.6 and 7.7
# Objective : Fill in the necessary areas to accurately use the library lp solve to get the results for the Linear it's Dual Program.
# Created by: Nicole Fleming
# Created on: 10/16/2020

# Import lpSolve package
library(lpSolve)

# Set coefficients of the objective function
f.obj <- c(-5, -3)

# Set matrix corresponding to coefficients of constraints by rows
# Do not consider the non-negative constraint; it is automatically assumed
f.con <- matrix(c(2,  2,
                  2, -4,
                  -2, 1,
                  0, -1,
                  0,  1), nrow = 5, byrow = TRUE)

# Set unequality signs
f.dir <- c("<=",
           "<=",
           "<=",
           "<=",
           "<=")

# Set right hand side coefficients
f.rhs <- c(33,
           8,
           5,
          -1,
           8)

# Final value (z)
lp("min", f.obj, f.con, f.dir, f.rhs)

# Variables final values
lp("min", f.obj, f.con, f.dir, f.rhs)$solution

# Sensitivities
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.from
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$sens.coef.to

# Dual Values (first dual of the constraints and then dual of the variables)
# Duals of the constraints and variables are mixed
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals

# Duals lower and upper limits
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.from
lp("min", f.obj, f.con, f.dir, f.rhs, compute.sens=TRUE)$duals.to

