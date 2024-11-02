
# main to test the simulator
from module_parser import parse_module  
from stim_parser import parse_stim  
from simulation import simulator

#circuit and stimuli files to be parsed
circuit_file = "/Users/farahmarei/Desktop/project_copy/tests/circuit2.v"  
stimuli_file = "/Users/farahmarei/Desktop/project_copy/tests/circuit_2.stim"  
parsed_circuit = parse_module(circuit_file)
parsed_stimuli = parse_stim(stimuli_file)

#running the simulator
simulator = simulator(parsed_circuit, parsed_stimuli)
simulator.run_simulation()
simulator.write_simulation("circuit_output.sim")