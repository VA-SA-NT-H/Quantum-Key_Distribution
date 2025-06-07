from e91_simulator import run_e91_simulation
from metrics import calculate_chsh, calculate_qber, calculate_key_rate
from visualize import plot_chsh, plot_qber, plot_key_rate

if __name__ == "__main__":
    rounds = 1000
    results = run_e91_simulation(rounds)

    chsh_value = calculate_chsh(results)
    qber = calculate_qber(results)
    key_rate = calculate_key_rate(results, qber)

    print(f"\n✅ CHSH Value: {chsh_value:.3f} (Expected > 2)")
    print(f"✅ QBER: {qber * 100:.2f}%")
    print(f"✅ Final Key Rate: {key_rate:.3f}\n")

    # try:
    #     plot_chsh(results)
    #     plot_qber(results)
    #     plot_key_rate(key_rate)
    # except ModuleNotFoundError as e:
    #     print("❌ Visualization skipped: matplotlib is not installed.")
    #     print("To enable visualizations, run: pip install matplotlib")

    try:
        plot_chsh(results)
        plot_qber(results)
        plot_key_rate(key_rate)
    except ModuleNotFoundError:
        print("❌ Visualization skipped: matplotlib is not installed.")
        print("To enable visualizations, run: pip install matplotlib")
    except Exception as e:
        print(f"❌ Visualization error: {e}")
