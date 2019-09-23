# Irfansha Shaik, 13.09.2019, Aarhus.
# Naive encoding for Hamiltonian path

# Todos:
# 1. Check for test cases or benchmarks provided.
# 2. Handle other formats of graph inputs.
# 3. Add sample testcases.
# 4. Update comments.

import sys

def f_read(path):
    f = open(path, "r")
    f1 = f.readlines()
    temp_list = []
    global N,E
    N = int(f1.pop(0).strip())
    E = int(f1.pop(0).strip())
    for line in f1:
        line = line.strip().split()
        temp_list.append(line)
    return temp_list


def AMO(var):
    # just an example appending for now
    for i in range(0, len(var)):
        for j in range(i + 1, len(var)):
            cnf_output.append([-var[i], -var[j], 0])


# Takes a set of variables as input and appends the clause to the main output vector.
def ALO(var):
    var.append(0)
    cnf_output.append(var)

def edg_con(lst):
    inv = int(lst.pop(0))
    for i in range(1,N):
        temp_clause = [-var_map(i, inv)]
        for outv in lst:
            temp_clause.append(var_map(i+1,int(outv)))
        temp_clause.append(0)
        cnf_output.append(temp_clause)


def var_map(i, j):
    return ((i - 1) * N + j)


def convert(lst):
    s = [str(i) for i in lst]
    return ' '.join(s)


def print_cnf(opt):
    print("p cnf " + str(N * N) + " " + str(len(cnf_output)))
    if (opt == "q"):
        st = "e "
        for i in range(1, N*N+1):
          st += str(i) + " "
        st += "0"
        print(st)
    for line in cnf_output:
        print(convert(line))

N = 0
E = 0
cnf_output = []


def main(argv):
    if (len(sys.argv) != 3):
        print("Use command: python naive_encoding.py [path-to-input-graph] [s/q]")
        print("s: for SAT encoding and q for QBF encoding")
    else:
      path = sys.argv[1]
      option = sys.argv[2]
      # print(option)
      # print("N = "+str(N))
      adj_list = f_read(path)
      # print(adj_list)

      # Exactly one node each turn:
      for i in range(1, N + 1):
        temp_var = []
        for j in range(1, N + 1):
            temp_var.append(var_map(i, j))
        AMO(temp_var)

      for i in range(1, N + 1):
        temp_var = []
        for j in range(1, N + 1):
            temp_var.append(var_map(i, j))
        ALO(temp_var)

      # Visit every vertex only once:
      for j in range(1, N + 1):
        temp_var = []
        for i in range(1, N + 1):
            temp_var.append(var_map(i, j))
        AMO(temp_var)

      for j in range(1, N + 1):
        temp_var = []
        for i in range(1, N + 1):
            temp_var.append(var_map(i, j))
        ALO(temp_var)

      # Edge constraints:
      for ver in adj_list:
        edg_con(ver)
      print_cnf(option)


if __name__ == "__main__":
    main(sys.argv[1:])
