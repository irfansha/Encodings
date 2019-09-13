# Irfansha Shaik, 13.09.2019, Aarhus.
# Naive encoding for Hamiltonian path
# Developement in two stages:
# First stage:
# Take N as input and outputs N exactly one constraints for N levels using N^2 variables.
# Second stage:
# Takes additional graph input to add required additional clauses.

# Todos:
# 1. Add AMO constraint function
#   - Takes a set of variables as input and appends clauses to the main output vector.
# 2. Add ALO constraint function

import sys


def AMO(var):
    temp_cnf = []
    # just an example appending for now
    for i in var:
        temp_cnf.append(i)
    cnf_output.append(temp_cnf)


# Takes a set of variables as input and appends the clause to the main output vector.
def ALO(var):
    cnf_output.append(var)

def var_map(i,j,N):
    return ((i-1)*N + j)

cnf_output = []

def main(argv):
    N = int(sys.argv[1])
    print("N = "+str(N))
    # AMO([1,2])
    # ALO([1,2])
    for i in range(1,N+1):
        temp_var = []
        for j in range(1,N+1):
            temp_var.append(var_map(i,j,N))
        ALO(temp_var)
    print(cnf_output)

if __name__ == "__main__":
   main(sys.argv[1:])
