# Floating Point MAC Hardware Accelerator

This repository implements a hardware accelerator for the Multiply-Accumulate (MAC) operation using Verilog and Python-based simulation with Cocotb. The MAC operation is a fundamental building block in many digital signal processing (DSP) and machine learning applications. This project provides a hardware implementation of the MAC operation and integrates it with a Python-based testbench for simulation and verification.

---

## Table of Contents
1. [Folder Structure](#folder-structure)
2. [Cocotb File Structure](#cocotb-file-structure)
3. [Verilog File Descriptions](#verilog-file-descriptions)
4. [Detailed Explanation of `MAC32_top.v`](#detailed-explanation-of-mac32_topv)
5. [How `main_MAC_test.py` Calls `MAC32_top.v`](#how-main_mac_testpy-calls-mac32_topv)
6. [What is a MAC Operation?](#what-is-a-mac-operation)

---

## Folder Structure

The repository is organized as follows:
```
Floating_Point_MAC_HW_Accelerator/ 
   ├── RTL/ # Contains all Verilog files for the hardware implementation 
      ├── MAC32_top.v # Top-level module for the MAC operation 
      ├── LeadingOneDetector_Top.v # Leading-one detector for normalization 
      ├── Normalizer.v # Normalizes the mantissa and adjusts the exponent 
      ├── PreNormalizer.v # Prepares inputs for normalization 
      ├── R4Booth.v # Radix-4 Booth multiplier for partial product generation 
   ├── main_MAC_test.py # Python testbench for the MAC operation 
   ├── test_MAC32.py # Cocotb testbench for MAC32_top.v 
   ├── sim_build/ # Temporary build folder for simulation (ignored in .gitignore) 
   ├── pycache/ # Python bytecode cache (ignored in .gitignore) 
```

## Cocotb File Structure

Cocotb is used for Python-based simulation and verification of the Verilog modules. Below is the structure of the Cocotb files and their interactions:

1. **`main_MAC_test.py`**:
   - This is the main Python script that initializes the simulation.
   - It sets up the test environment and calls the Cocotb testbench (`test_MAC32.py`).

2. **`test_MAC32.py`**:
   - This is the Cocotb testbench for the `MAC32_top.v` module.
   - It interacts with the Verilog module by driving inputs and monitoring outputs.
   - Calls the `MAC32_top.v` module for hardware acceleration of the MAC operation.

---

## Verilog File Descriptions

### 1. `MAC32_top.v`
- **Purpose**: This is the top-level module for the MAC operation. It integrates all the submodules required for the MAC operation, including multiplication, addition, and normalization.
- **Inputs**:
  - `a`, `b`, `c`: Floating-point operands for the MAC operation.
- **Outputs**:
  - `result`: The result of the MAC operation (`a + b * c`).
- **Submodules**:
  - `R4Booth.v`: Performs partial product generation for multiplication.
  - `PreNormalizer.v`: Prepares the inputs for normalization.
  - `Normalizer.v`: Normalizes the mantissa and adjusts the exponent.
  - `LeadingOneDetector_Top.v`: Detects the position of the leading one for normalization.

### 2. `R4Booth.v`
- **Purpose**: Implements the Radix-4 Booth algorithm for efficient multiplication.
- **Functionality**:
  - Generates partial products based on Booth encoding.
  - Handles sign correction for negative partial products.

### 3. `PreNormalizer.v`
- **Purpose**: Prepares the inputs for normalization by aligning the mantissa and exponent.
- **Functionality**:
  - Aligns the mantissa based on the exponent movement.
  - Calculates the aligned exponent and sticky bits.

### 4. `Normalizer.v`
- **Purpose**: Normalizes the mantissa and adjusts the exponent to ensure the result is in IEEE-754 format.
- **Functionality**:
  - Performs left shifts on the mantissa.
  - Adjusts the exponent based on the shift amount.

### 5. `LeadingOneDetector_Top.v`
- **Purpose**: Detects the position of the leading one in the mantissa for normalization.
- **Functionality**:
  - Uses hierarchical zero detectors to efficiently find the leading one.

---

## Detailed Explanation of `MAC32_top.v`

The `MAC32_top.v` module is the heart of the hardware accelerator. It performs the MAC operation (`result = a + b * c`) in the following steps:

1. **Multiplication**:
   - The `R4Booth.v` module generates partial products for the multiplication of `b` and `c`.
   - These partial products are summed to produce the intermediate product.

2. **Addition**:
   - The intermediate product is added to `a` to compute the MAC result.

3. **Normalization**:
   - The `PreNormalizer.v` and `Normalizer.v` modules ensure the result is in IEEE-754 format by aligning and normalizing the mantissa and adjusting the exponent.

4. **Leading-One Detection**:
   - The `LeadingOneDetector_Top.v` module detects the position of the leading one in the mantissa to determine the normalization shift.

---

## How `main_MAC_test.py` Calls `MAC32_top.v`

1. **Initialization**:
   - The `main_MAC_test.py` script initializes the simulation environment using Cocotb.

2. **Testbench Setup**:
   - The script calls the `test_MAC32.py` testbench, which interacts with the `MAC32_top.v` module.

3. **Input Stimuli**:
   - The testbench drives inputs (`a`, `b`, `c`) to the `MAC32_top.v` module.

4. **Output Monitoring**:
   - The testbench monitors the output (`result`) from the `MAC32_top.v` module and compares it with the expected result.

5. **Verification**:
   - The testbench verifies the correctness of the hardware implementation by comparing the hardware result with the software-calculated result.

---

## What is a MAC Operation?

The Multiply-Accumulate (MAC) operation is a fundamental arithmetic operation used in many applications, including DSP and machine learning. It performs the following computation:

### How It Is Done Here:
1. **Inputs**:
   - `a`, `b`, and `c` are floating-point numbers in IEEE-754 format.

2. **Steps**:
   - The `b * c` multiplication is performed using the `R4Booth.v` module.
   - The result of the multiplication is added to `a` using an adder.
   - The result is normalized to ensure it conforms to the IEEE-754 format.

3. **Output**:
   - The final result is a floating-point number in IEEE-754 format.

---

### Credits and Sources

- This project is heavily inspired by the work of (https://github.com/hankshyu/RISC-V_MAC.git).
- However, the code is highly customized and altered using LLM to fit the specific requirements of this project.
- Also, the implementation is tailored for this specific use case of cocotb. 
- The project is open-source and available for further development and contributions.