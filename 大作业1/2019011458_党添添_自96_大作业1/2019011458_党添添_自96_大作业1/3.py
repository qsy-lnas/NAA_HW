import numpy as np
import copy
lines = []
with open("regression.txt","r") as file:
    for line in file:
        line = line.split(" ")
        temp = copy.deepcopy(line[0:3])
        lines.append(temp)

X = np.zeros(len(lines))
Y = np.zeros(len(lines))
Z = np.zeros(len(lines))

for idx,inst in enumerate(lines):
    Y[idx]  =  -float(inst[1])*float(inst[1])*float(inst[2])*float(inst[2])*float(inst[2])
    X[idx] = float(inst[0])*float(inst[0])*float(inst[2])*float(inst[2])*float(inst[2])
    Z[idx] = (2.0*float(inst[0])*float(inst[0])+float(inst[1])*float(inst[1])+float(inst[2])*float(inst[2])-1)**3

a_1 = np.dot(X,Y)/np.dot(X,X)
b_1 = Y.mean() - a_1*X.mean()




b = Z.mean()/b_1
a = a_1*b
a_1 = round(a_1,2)
b_1 = round(b_1,2)
a = round(a,2)
b = round(b,2)
print("a1 = {}\nb1 = {}".format(a_1,b_1))
print("a = {}\nb = {}".format(a,b))
