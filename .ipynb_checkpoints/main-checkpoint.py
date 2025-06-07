from e91_simulator import run_e91_simulation
from metrics import calculate_chsh, calculate_qber, calculate_key_rate, final_key
from visualize import plot_chsh, plot_qber, plot_key_rate

if __name__ == "__main__":
    rounds = int(input("Enter number of rounds (default 1000): ") or 1000)
    results = run_e91_simulation(rounds)
    print(results)
    matched_bits = 0
    
    chsh_value = calculate_chsh(results)
    qber = calculate_qber(results, matched_bits)
    key_rate = calculate_key_rate(results, qber, rounds, matched_bits)
    secret_key = final_key(results)

    print(f"Final secret key : {secret_key}")
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
