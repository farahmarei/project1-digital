import heapq  

class simulator:
    def __init__(self, c, e):
        self.circuit = c  
        self.stim_events = e  
        self.event_queue = []  
        self.signal_values = {}  # dictionary storing the variables and their values
        self.sim_output = []  # stores the output events

    def initialize(self):
        for var in self.circuit.inputs:
            self.signal_values[var] = 0 # initialize all inputs to 0
        for var in self.circuit.wires:
            self.signal_values[var] = 0
        for var in self.circuit.outputs:
            self.signal_values[var] = 0
        
    def load(self):
        for event in self.stim_events.events:
            timing, var, value = event 
            heapq.heappush(self.event_queue, (timing, var, value)) # adding the initial events to a priority queue

    def process(self, time, var, new_value):
        variable = [gate.display() for gate in self.circuit.gates]
        print(variable)
        if self.signal_values[var] != new_value:
            self.signal_values[var] = new_value # assign new value to the variable
            self.sim_output.append((time, var, new_value)) # add the new change to the output file
            print(time,var,new_value)
            # look for all gates impacted by variable change
            changed_gates = [gate for gate in self.circuit.gates if var in (gate.inputs)]  # a gate is affected if it has the variable as an input
            for gate in changed_gates:
                print(gate.inputs)
                self.propagate(gate, time)

    def propagate(self, gate, current_time):
        gate_type, delay_time, inputs, output = gate.gate_type, gate.delay_time, gate.inputs, gate.output
    
        # get current inputs of the gate
        print("my inputs",inputs)
        current_inputs = [self.signal_values[input_signal] for input_signal in inputs] 
        # get new output value depending on the type of gate
        new_output = self.output_gate(gate_type, current_inputs)
        
        
        if self.signal_values[output] != new_output: #if the output changes
            event_time = current_time + delay_time 
            heapq.heappush(self.event_queue, (event_time, output, new_output)) # push changed output

    def output_gate(self, gate_type, current_inputs):
        if gate_type == 'and':
            return int(all(current_inputs)) # python function that return 1 if all inputs are 1
        elif gate_type == 'or':
            return int(any(current_inputs)) # python function that return 1 if at least one input is 1
        elif gate_type == 'nand':
            return int(not all(current_inputs)) # not and
        elif gate_type == 'nor':
            return int(not any(current_inputs)) # not or
        elif gate_type == 'xor':
            return int(current_inputs[0] != current_inputs[1]) # both inputs should be different
        elif gate_type == 'xnor':
            return int(current_inputs[0] == current_inputs[1]) # if both are 0 or both are 1
        elif gate_type == 'not':
            return int(not current_inputs[0]) #python function to invert
        elif gate_type == 'buf':
            return current_inputs[0] 
        return 0

    def run_simulation(self):
        #initalize and load
        self.initialize()
        self.load()

        #process every event in the priority queue(pops the event with the smallest time)
        while self.event_queue:
            time, signal, value = heapq.heappop(self.event_queue)
            self.process(time, signal, value)

    def write_simulation(self, filename="output.sim"):
        with open(filename, 'w') as file:
            for time, signal, value in self.sim_output:
                file.write(f"{time}, {signal}, {value}\n") #write each event in the output file
        print(f"Simulation has been written to {filename}")


