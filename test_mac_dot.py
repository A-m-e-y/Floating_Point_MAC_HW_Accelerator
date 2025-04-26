import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "input_buffer.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "output_buffer.txt")

def float_to_bits(f):
    float_bytes = np.float32(f).tobytes()
    return BinaryValue(value=int.from_bytes(float_bytes, byteorder='little'), n_bits=32, bigEndian=False)

def bits_to_float(b):
    return np.frombuffer(np.uint32(int(b)).tobytes(), dtype=np.float32)[0]

@cocotb.test()
async def test_mac_scalar(dut):
    # No clock — pure combo logic
    with open(INPUT_FILE, "r") as f:
        line = f.readline().strip()
        a, b, c = map(float, line.split())

    # Apply inputs
    dut.A_i.value = float_to_bits(a)
    dut.B_i.value = float_to_bits(b)
    dut.C_i.value = float_to_bits(c)
    # dut.Rounding_mode_i.value = 0b011

    # Wait for logic to settle
    await Timer(1, units="ns")

    # Read result
    result = bits_to_float(dut.Result_o.value)

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"{result:.8f}\n")

