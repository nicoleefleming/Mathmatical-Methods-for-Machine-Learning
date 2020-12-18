# Title     : Use Quadratic Programming to solve for the Primal and Dual Programs presented in 7.6 and 7.7
# Objective : Fill in the necessary areas to accurately use the library quadprog and solve.QP to
#             get the results for the Quadratic it's Dual Program.
# Created by: Nicole Fleming
# Created on: 10/16/2020

# Import quadprog library
library(quadprog)

# Matrix appearing in the quadratic function
Dmat <- matrix(c(2, 4, 1, 4), 2, 2)

# Vector appearing in the quadratic function
dvec <- c(5, 3)

# Matrix defining the constraints
Amat <- t(matrix(c(1, 0,
                   -1, 0,
                   0, 1,
                   0, -1), 4, 2))

# Vector holding the value of b_0
bvec <- c(1, 1, 1, 1)

# Only the first constraint is equality
qp <- solve.QP(Dmat, dvec, Amat, bvec, meq = 1)
qp