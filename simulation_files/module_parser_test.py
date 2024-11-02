# parse the module (for testing)

from module_parser import parse_module

#testing first circuit
circuit = parse_module("/Users/farahmarei/Desktop/project1-digital/tests/circuit1.v")

# Display parsed circuit information
print(circuit.display())
print(circuit.gates[0].display())