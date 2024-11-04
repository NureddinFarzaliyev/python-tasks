
import numpy as np

a = np.array([[0,0], [1,0], [0,1], [1,1]])

def print_table(METHOD):
    print("Truth Table for " + METHOD)
    for i in a:
        if METHOD == "NOR": v_or = i[0] or i[1]
        elif METHOD == "XOR": v_or = i[0] == i[1]
        elif METHOD == "XNOR": v_or = i[0] != i[1]
        print(i[0], i[1], sep='', end=' -> ')
        if v_or == 1: print(0)
        else: print(1)

print_table("XOR")
print_table("NOR")
print_table("XNOR")
 