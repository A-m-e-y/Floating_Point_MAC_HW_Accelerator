import numpy as np
from hw_wrapper import hw_mac

def sw_mac(a, b, c):
    return float(a + b * c)

def run_test():
    passed = 0
    failed = 0
    N = 10

    for i in range(N):
        a = np.round(np.random.uniform(-5.0, 5.0), 4)
        b = np.round(np.random.uniform(-5.0, 5.0), 4)
        c = np.round(np.random.uniform(-5.0, 5.0), 4)

        sw_result = sw_mac(a, b, c)
        hw_result = hw_mac(a, b, c)

        print(f"\nTest {i+1}")
        print(f"A     : {a}")
        print(f"B     : {b}")
        print(f"C     : {c}")
        print(f"SW    : {sw_result}")
        print(f"HW    : {hw_result}")

        if abs(hw_result - sw_result) < 1e-3:
            print("✅ PASS")
            passed += 1
        else:
            print("❌ FAIL")
            failed += 1

    print(f"\nTotal: {N}, Passed: {passed}, Failed: {failed}")

if __name__ == "__main__":
    run_test()

