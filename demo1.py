# Step 1: Import required libraries
import numpy as np
import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Step 2: Define Alice and Bob’s measurement angles (in radians)
alice_angles = [0, np.pi/4]        # 0° and 45°
bob_angles = [np.pi/4, np.pi/2]    # 45° and 90°

# Step 3: Initialize shared key storage
shared_key = []

# Step 4: Setup simulator
simulator = Aer.get_backend('qasm_simulator')

# Step 5: Repeat for 10 rounds
for i in range(10):
    print(f"\n🔁 Round {i+1}")

    # Step 5.1: Create entangled pair |Φ+⟩ = (|00⟩ + |11⟩)/√2
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)

    # Step 5.2: Randomly pick measurement angles
    a_angle = random.choice(alice_angles)
    b_angle = random.choice(bob_angles)

    print(f"Alice angle: {round(np.degrees(a_angle))}°, Bob angle: {round(np.degrees(b_angle))}°")

    # Step 5.3: Apply rotations to align to chosen basis
    qc.ry(-2 * a_angle, 0)
    qc.ry(-2 * b_angle, 1)

    # Step 5.4: Measure both qubits
    qc.measure(0, 0)
    qc.measure(1, 1)

    # Step 5.5: Run on simulator
    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=1, memory=True)
    result = job.result()
    output = result.get_memory()[0]

    # Step 5.6: Extract measurement results
    a_result = int(output[1])  # Alice’s bit
    b_result = int(output[0])  # Bob’s bit
    print(f"Alice measured: {a_result}, Bob measured: {b_result}")

    # Step 5.7: Extract key bit only if (0°, 45°)
    strong_correl = -np.cos(2*(a_angle - b_angle))
    # print(f"Correlation of {np.degrees(a_angle)}° & {np.degrees(b_angle)}°")
    print(f"Correlation of {round(np.degrees(a_angle))}° & {round(np.degrees(b_angle))}° = {strong_correl}")
    # if strong_correl == -1.0 or strong_correl == +1.0:
    if np.isclose(abs(strong_correl), 1.0, atol=1e-8):
        key_bit = a_result ^ b_result
        shared_key.append(key_bit)
        print(f"✅ Shared key bit added: {key_bit}")
    else:
        print("❌ Basis mismatch — no key bit")

print("\n🔐 Final Shared Key:", shared_key)

