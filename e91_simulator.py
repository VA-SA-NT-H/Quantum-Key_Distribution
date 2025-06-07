import numpy as np
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

alice_angles = [0, np.pi/4, np.pi/2]
bob_angles = [np.pi/4, np.pi/2, 3*np.pi/4]
simulator = AerSimulator()

def create_bell_pair():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def measure_in_basis(qc, qubit, angle):
    qc.ry(-2 * angle, qubit)
    qc.measure(qubit, qubit)

def run_e91_simulation(n):
    data = []
    for _ in range(n):
        qc = create_bell_pair()

        a_idx = random.randint(0, 2)
        b_idx = random.randint(0, 2)
        a_angle = alice_angles[a_idx]
        b_angle = bob_angles[b_idx]

        measure_in_basis(qc, 0, a_angle)
        measure_in_basis(qc, 1, b_angle)

        tqc = transpile(qc, simulator)
        result = simulator.run(tqc, shots=1).result()
        counts = result.get_counts()
        outcome = list(counts.keys())[0]

        data.append({
            "alice_angle_idx": a_idx,
            "bob_angle_idx": b_idx,
            "outcome": outcome
        })
    return data