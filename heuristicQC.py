from qiskit import QuantumCircuit            #Qiskit tools importing
from qiskit import *
from mqt import qmap                         #MQT tools of QMAP importing
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import circuit_drawer
import os

arch = qmap.Architecture(5,{                 #5 qubit manual random arbitrary quantum architecture formed
    (1, 0), (2, 0), 
    (2, 1), (3, 2), 
    (3, 4), (2, 4)})

with open("qc1.txt") as f:                   #input file of quantum circuit is called
    f = f.read()                             #convert .txt file into string format
    n = len(f)                               
qc1 = f[0:n]                                 #quantum circuit is stored in string format

with open("qc2.txt") as f:                   
    f = f.read()
    n = len(f)
qc2 = f[0:n]                                 

with open("qc3.txt") as f:                   
    f = f.read()
    n = len(f)
qc3 = f[0:n]                                 

with open("qc4.txt") as f:                   
    f = f.read()
    n = len(f)
qc4 = f[0:n]                                 

with open("qc5.txt") as f:                   
    f = f.read()
    n = len(f)
qc5 = f[0:n]                                 

with open("qc6.txt") as f:                   
    f = f.read()
    n = len(f)
qc6 = f[0:n]                                 

with open("qc7.txt") as f:                   
    f = f.read()
    n = len(f)
qc7 = f[0:n]                                 

with open("qc8.txt") as f:                   
    f = f.read()
    n = len(f)
qc8 = f[0:n]                                 

with open("qc9.txt") as f:                   
    f = f.read()
    n = len(f)
qc9 = f[0:n]                                 

with open("qc10.txt") as f:                   
    f = f.read()
    n = len(f)
qc10 = f[0:n]                                 

circuits = [qc1, qc2, qc3, qc4, qc5, qc6, qc7, qc8, qc9, qc10]       #grouping of quantum circuit for automation process

c=1
for i in circuits:                                       #automation process
    output_file = os.path.join('output', i)
    print("initial circuit ",c)
    circ = QuantumCircuit.from_qasm_str(i)               #forming quantum circuit
    print(circ)                                          #visualizing quantum circuit
    transpiled_circuit = transpile(circ)
    circuit_image = circuit_drawer(transpiled_circuit)
    output_path = f"{'output'}/{i}.png"
    circuit_image.savefig(output_path)                   #save quantum circuit as .png
    print("\n")
    print("heuristic circuit ",c)
    qc_m , res = qmap.compile(circ, arch , method="heuristic")            #forming heuristic mapping quantum circuit
    print(qc_m)                                                           #visualizing heuristic mapping quantum circuit
    transpiled_circuit = transpile(qc_m)
    circuit_image = circuit_drawer(transpiled_circuit)
    output_path = f"{'output'}/{i}.png"
    circuit_image.savefig(output_path)                   ##save quantum circuit heuristic mapping as .png
    print("\n\n\n\n")
    c+=1