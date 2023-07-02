from qiskit import QuantumCircuit                     #Qiskit tools importing
from qiskit import *
from mqt import qmap                                  #MQT tools of QMAP importing

arch = qmap.Architecture(5,{                          #5 qubit manual random arbitrary quantum architecture formed
    (1, 0), (2, 0), 
    (2, 1), (3, 2), 
    (3, 4), (2, 4)})

f1 = open("input.txt","r")                            #input file of quantum circuit is called

c=1
for line in f1:                                       #automation process
    print("initial circuit ",c)
    circ = QuantumCircuit.from_qasm_str(line)         #forming quantum circuit
    print(circ)                                       #visualizing quantum circuit
    print("\n")
    print("heuristic circuit ",c)
    qc_m , res = qmap.compile(circ, arch , method="heuristic")            #forming heuristic mapping quantum circuit
    print(qc_m)                                                           #visualizing heuristic mapping quantum circuit
    print("\n\n\n\n")
    c+=1
    
f1.close()                                            #closing file
