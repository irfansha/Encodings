# Irfansha Shaik, 13.09.2019, Aarhus.
# Naive encoding for Hamiltonian path
# Developement in two stages:
# First stage:
# Take N as input and outputs N exactly one constraints for N levels using N^2 variables.
# Second stage:
# Takes additional graph input to add required additional clauses.

# Todos:
# 1. Add comments in the printing output.

import sys


def AMO(var):
    temp_cnf = []
    # just an example appending for now
    for i in range(0,len(var)):
        for j in range(i+1, len(var)):
            cnf_output.append([-var[i],-var[j],0])


# Takes a set of variables as input and appends the clause to the main output vector.
def ALO(var):
    var.append(0)
    cnf_output.append(var)

def var_map(i,j,N):
    return ((i-1)*N + j)

def convert(lst):
    s = [str(i) for i in lst]
    return ' '.join(s)

def print_cnf(N):
    print("p cnf " + str(N*N) + " " + str(len(cnf_output)))
    for line in cnf_output:
        print(convert(line))

cnf_output = []

def main(argv):
    N = int(sys.argv[1])
    # print("N = "+str(N))

    # AMO constraints:
    for i in range(1,N+1):
        temp_var = []
        for j in range(1,N+1):
            temp_var.append(var_map(i,j,N))
        AMO(temp_var)

    # ALO constraints:
    for i in range(1,N+1):
        temp_var = []
        for j in range(1,N+1):
            temp_var.append(var_map(i,j,N))
        ALO(temp_var)
    print_cnf(N)

if __name__ == "__main__":
   main(sys.argv[1:])
