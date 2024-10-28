import re
class Gate:
    def __init__(self,gate_name, gate_type,delay_time,inputs, output):
        self.gate_name = gate_name
        self.gate_type = gate_type
        self.delay_time = delay_time
        self.inputs = inputs
        self.output = output
        
    def display(self):
        return f"Gate(name={self.gate_name}, type={self.gate_type}, delay={self.delay_time}, inputs={self.inputs}, output={self.output})"
        
        
class Circuit:
    def __init__(self):
        self.inputs = []  
        self.outputs = []   
        self.gates = []
        self.wires = []
        
    def addgate(self,gate):
        self.gates.append(gate)
    
    def display(self):
        return (f"Circuit(inputs={self.inputs}, outputs={self.outputs}, "
                f"wires={self.wires}, gates={self.gates})")
                
                
def parse_verilog(verilog_file):
    
    circuit = Circuit()
    inputmatch = re.compile(r'^input\s+(.*);')
    outputmatch = re.compile(r'^output\s+(.*);')
    wirematch = re.compile(r'^wire\s+(.*);')
    gatematch = re.compile(r'(\w+)\s+#\((\d+)\)\s+(\w+)\s*\((\w+),\s*([\w, ]+)\);')
    
    with open(verilog_file, 'r') as file:
        for line in file:
            line = line.strip()
            if inputmatch.match(line):
                inputs = inputmatch.match(line).group(1)
                circuit.inputs.extend([inp.strip() for inp in inputs.split(',')])
            
            elif outputmatch.match(line):
                outputs = outputmatch.match(line).group(1)
                circuit.outputs.extend([out.strip() for out in outputs.split(',')])
                
            elif wirematch.match(line):
                wires = wirematch.match(line).group(1)
                circuit.wires.extend([wire.strip() for wire in wires.split(',')])
                
            elif gatematch.match(line):
                match = gatematch.match(line)
                gate_type = match.group(1)
                delay_time = int(match.group(2))
                gate_name = match.group(3)
                output = match.group(4)
                inputs = [inp.strip() for inp in match.group(5).split(',')]
                
                gate = Gate(gate_name,gate_type, delay_time, inputs, output) 
                circuit.addgate(gate)
                
                
        return circuit
                
        
                
                
                
                