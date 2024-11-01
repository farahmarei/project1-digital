import re

class stim_parser:
    def __init__(self,stimuli_file):
        self.stimuli_file = stimuli_file
        self.events = [] # list containing all events

    def display(self):
        print("Parsed Events:")
        for event in self.events:
            print(f"Time: {event[0]} ps, Signal: '{event[1]}', Value: {event[2]}")

def parse_stim(stimuli_file):

    stim = stim_parser(stimuli_file) # create an object
    eventregex = r"#(\d+)\s+(\w)=(\d);" # pattern of an event

    with open(stim.stimuli_file , 'r') as file:
        lines = file.readlines()
        for l in lines: # iterating through every line, stripping it
            line = l.strip()

            match =re.match(eventregex,line) # attempting to match the line to the regex pattern
            if match:
                time = int(match.group(1))
                signal = match.group(2)
                value = int(match.group(3))

                stim.events.append((time,signal,value)) # append to the list of events

    return stim