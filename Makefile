TOPLEVEL_LANG = verilog
# SIM = vcs
SIM = verilator
TOPLEVEL = MAC32_top
MODULE = test_mac_dot

# This tells VCS to use your file list
EXTRA_ARGS += -f files.list -sv -Wno-WIDTHEXPAND -Wno-WIDTHTRUNC

WAVES = 0  # Disable VCD unless needed

include $(shell cocotb-config --makefiles)/Makefile.sim

