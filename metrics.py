def calculate_chsh(data):
    counts = {(0, 0): [], (0, 1): [], (1, 0): [], (1, 1): []}

    for d in data:
        a, b = d["alice_angle_idx"], d["bob_angle_idx"]
        if (a, b) in counts:
            outcome = d["outcome"]
            if outcome == '00' or outcome == '11':
                counts[(a, b)].append(1)
            else:
                counts[(a, b)].append(-1)

    def mean(l): return sum(l)/len(l) if l else 0
    E = {key: mean(vals) for key, vals in counts.items()}

    S = abs(E[(0, 0)] - E[(0, 1)] + E[(1, 0)] + E[(1, 1)])
    return S

def calculate_qber(data):
    mismatch = total = 0
    for d in data:
        a, b = d["alice_angle_idx"], d["bob_angle_idx"]
        if a == b:
            total += 1
            if d["outcome"] not in ['00', '11']:
                mismatch += 1
    return mismatch / total if total > 0 else 0

def calculate_key_rate(data, qber):
    R0 = 0.5  # Raw key rate
    return R0 * (1 - 2 * qber)