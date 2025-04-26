import subprocess
import time
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "input_buffer.txt")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "output_buffer.txt")

def hw_mac(a, b, c):
    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)

    with open(INPUT_PATH, "w") as f:
        f.write(f"{a} {b} {c}\n")

    subprocess.run(["make", "sim"])

    start_time = time.time()
    while not os.path.exists(OUTPUT_PATH):
        if time.time() - start_time > 5:
            raise RuntimeError("Timeout waiting for output_buffer.txt from cocotb.")
        time.sleep(0.05)

    with open(OUTPUT_PATH, "r") as f:
        result = float(f.readline().strip())

    return result

