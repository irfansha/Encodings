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
#   - Takes a set of variables as input and appends the clause to the main output vector.

import sys

def AMO():
    print("In AMO function")

def ALO():
    print("In ALO function")

def main(argv):
    print("N = "+sys.argv[1])
    AMO()
    ALO()

if __name__ == "__main__":
   main(sys.argv[1:])