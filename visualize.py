try:
    import matplotlib
    import matplotlib.pyplot as plt
    interactive = matplotlib.get_backend().lower() not in ['agg', 'template']
except Exception:
    plt = None
    interactive = False


def plot_chsh(data):
    if plt is None:
        raise ModuleNotFoundError("matplotlib is not installed.")
    from metrics import calculate_chsh
    S = calculate_chsh(data)
    plt.axhline(y=2, color='r', linestyle='--', label='Classical Limit')
    plt.bar(["CHSH"], [S], color='green')
    plt.title("CHSH Violation")
    plt.ylim(0, 4)
    plt.legend()
    if interactive:
        plt.show()
    else:
        print("⚠️ Matplotlib backend is non-interactive. Cannot display plot.")


def plot_qber(data):
    if plt is None:
        raise ModuleNotFoundError("matplotlib is not installed.")
    from metrics import calculate_qber
    qber = calculate_qber(data)
    plt.bar(["QBER"], [qber * 100], color='orange')
    plt.title("Quantum Bit Error Rate (%)")
    plt.ylim(0, 100)
    if interactive:
        plt.show()
    else:
        print("⚠️ Plot not shown (non-interactive backend or headless mode).")


def plot_key_rate(rate):
    if plt is None:
        raise ModuleNotFoundError("matplotlib is not installed.")
    plt.bar(["Key Rate"], [rate], color='blue')
    plt.title("Final Usable Key Rate")
    plt.ylim(0, 1)
    if interactive:
        plt.show()
    else:
        print("⚠️ Plot not shown (non-interactive backend or headless mode).")
