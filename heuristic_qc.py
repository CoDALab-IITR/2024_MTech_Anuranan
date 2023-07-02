from qiskit import QuantumCircuit
from qiskit import *
from mqt import qmap

arch = qmap.Architecture(5,{
    (1, 0), (2, 0), 
    (2, 1), (3, 2), 
    (3, 4), (2, 4)})

f1 = open("input.txt","r")

c=1
for line in f1:
    f2 = open("output.txt","a")
    print("initial circuit ",c)
    circ = QuantumCircuit.from_qasm_str(line)
    f2.write(circ)
    f2.write("\n")
    #print(circ)
    #print("\n")
    print("heuristic circuit ",c)
    qc_m , res = qmap.compile(circ, arch , method="heuristic")
    f2.write(qc_m)
    f2.write("\n\n\n\n")
    #print(qc_m)
    #print("\n\n\n\n\n")
    c+=1
    f2.close()
    
f1.close()