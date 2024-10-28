parse_verilog_test

from verilog_parser import parse_verilog

circuit = parse_verilog("circuit_1.v")

# Display parsed circuit information
print(circuit.display())