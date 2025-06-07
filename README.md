# 🔐 Bell Inequality Violation Analyzer (BIVA)

A simulation tool for the **E91 Protocol** in Quantum Key Distribution (QKD).

## 📌 Features

- Create Bell states for entangled qubits
- Randomly assign measurement angles
- Calculate:
  - ✅ CHSH Violation Value
  - ✅ Quantum Bit Error Rate (QBER)
  - ✅ Usable Key Rate
- Visualize results with Matplotlib (optional)

## 🚀 Run the Project

```bash
pip install qiskit numpy matplotlib
python main.py
```

If you do not have `matplotlib`, the program will still run, but visualizations will be skipped.

## 📊 Sample Output

```
✅ CHSH Value: 2.824 (Quantum Entanglement)
✅ QBER: 0.00%
✅ Final Key Rate: 0.500
```