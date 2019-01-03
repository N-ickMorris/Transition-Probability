# the following is a script that raises a matrix to a power
# import sympy and some functions
import sympy as sp
from sympy import MatrixSymbol, Matrix

# define alpha (a)
# define beta (b)
# define step constant (k)
# define transition probability matrix (P)
a = sp.Symbol('a')
b = sp.Symbol('b')
k = sp.Symbol('k')
P = Matrix(MatrixSymbol('P', 2, 2))

# update P
P[0,0] = 1 - a
P[0,1] = a
P[1,0] = b
P[1,1] = 1 - b

# compute the k step transition probability matrix
P**k

# --------------------------------------------------------------

# the following is a script to solve a system of equations
# import sympy
# import sympy as sp

# define the mean number of times the target is hit when player 1 shoots first (m1)
# define the mean number of times the target is hit when player 2 shoots first (m2)
# define the probability of player 1 hitting the target (p1)
# define the probability of player 2 hitting the target (p2)
# define the probability of player 1 missing the target (q1)
# define the probability of player 2 missing the target (q2)
m1 = sp.Symbol('m1')
m2 = sp.Symbol('m2')
p1 = sp.Symbol('p1')
p2 = sp.Symbol('p2')
q1 = sp.Symbol('q1')
q2 = sp.Symbol('q2')

# define the two equations for m1 and m2
eqns = [sp.Eq((2 * p1 * p2) + ((2 + m1) * p1 * q2) + ((1 + m2) * q1) - m1),
sp.Eq((2 * p2 * p1) + ((2 + m2) * p2 * q1) + ((1 + m1) * q2) - m2)]

# define the two variables that we are solving for (ie. m1 and m2)
varlist = [m1, m2]

# solve the system of two equations
sol = sp.solve(eqns, varlist)
sol
