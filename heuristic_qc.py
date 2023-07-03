from qiskit import QuantumCircuit            #Qiskit tools importing
from qiskit import *
from mqt import qmap                         #MQT tools of QMAP importing

arch = qmap.Architecture(5,{                 #5 qubit manual random arbitrary quantum architecture formed
    (1, 0), (2, 0), 
    (2, 1), (3, 2), 
    (3, 4), (2, 4)})

f = open("qc1.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc2.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc3.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc4.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc5.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc6.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc7.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc8.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc9.txt","r")                      #input file of quantum circuit is called

f.close() 

f = open("qc10.txt","r")                     #input file of quantum circuit is called

f.close() 

circuits = [qc1, qc2, qc3, qc4, qc5, qc6, qc7, qc8, qc9, qc10]       #grouping of quantum circuit

c=1
for i in circuits:                                       #automation process
    print("initial circuit ",c)
    circ = QuantumCircuit.from_qasm_str(i)               #forming quantum circuit
    print(circ)                                          #visualizing quantum circuit
    print("\n")
    print("heuristic circuit ",c)
    qc_m , res = qmap.compile(circ, arch , method="heuristic")            #forming heuristic mapping quantum circuit
    print(qc_m)                                                           #visualizing heuristic mapping quantum circuit
    print("\n\n\n\n")
    c+=1