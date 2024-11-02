import re
class Gate:
    def __init__(self,n, t,d, i, o):
        self.gate_name = n
        self.gate_type = t
        self.delay_time = d
        self.inputs = i
        self.output = o
        
    def display(self):
        # Displaying the gate details
        return f"Gate(name={self.gate_name}, type={self.gate_type}, delay={self.delay_time}, inputs={self.inputs}, output={self.output})"
        
        
class Circuit:
    def __init__(self):
        self.inputs = []  # array containing all inputs to the circuit
        self.outputs = [] # array containing all outputs from the circuit
        self.gates = [] 
        self.wires = []
        
    def addgate(self,gate):
        # adds a new gate to the circuit 
        self.gates.append(gate)
    
    def display(self):
        return (f"Circuit(inputs={self.inputs}, outputs={self.outputs}, "
                f"wires={self.wires}, gates={self.gates})")
                
                
def parse_module(v_file):
    circuit = Circuit() # create a circuit object to be passed to the main program

     # creates regex pattern to match those in the .v file
    inputregex = re.compile(r'^input\s+(.*);') 
    outputregex = re.compile(r'^output\s+(.*);')
    wireregex = re.compile(r'^wire\s+(.*);')
    gateregex = re.compile(r'(\w+)\s+#\((\d+)\)\s+(\w+)\s*\((\w+),\s*([\w, ]+)\);')
    
    with open(v_file, 'r') as file:
 
        for line in file: # looping over every line
            input_arr = []
            output_arr = []
            gate_inputs = [] 
            wire_arr = [] 

            line = line.strip() # remove any whitespaces
            if inputregex.match(line):
                inputs = inputregex.match(line).group(1)
                input_names = inputs.split(',') # split inputs by comma into list

                for inp in input_names:
                    input_arr.append(inp.strip()) # add the inputs to the list after striping
                circuit.inputs.extend(input_arr) 
            
            elif outputregex.match(line):
                outputs = outputregex.match(line).group(1)
                output_names = outputs.split(',') 
                for out in output_names:
                    output_arr.append(out.strip()) 
                circuit.outputs.extend(output_arr)
                
            elif wireregex.match(line):
                wires = wireregex.match(line).group(1)
                wire_names = wires.split(',') 
                for w in wire_names:
                    wire_arr.append(w.strip()) 
                circuit.wires.extend(wire_arr)
                
            elif gateregex.match(line):
                gate = gateregex.match(line)
                # divide the parsed line into required fields ( type,delay,name,etc.)
                gate_type = gate.group(1) 
                delay_time = int(gate.group(2))
                gate_name = gate.group(3)
                output = gate.group(4)

                input_names = gate.group(5).split(',') # split inputs by comma into list
                for inp in input_names:
                    gate_inputs.append(inp.strip())
                            
                gate = Gate(gate_name,gate_type, delay_time, gate_inputs, output) #create the object
                circuit.addgate(gate) # add to the circuit
                
                
        return circuit 
                
        
                
                
                
                
