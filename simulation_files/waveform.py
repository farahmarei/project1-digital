#wave form visualization
import matplotlib.pyplot as plt
import pandas as pd

def plot_waveform(simulation_file):
    # loading data from output.sim 
    data = pd.read_csv(simulation_file, header=None, names=["Time", "Signal", "Value"])

    # extracting unique signals/variables (a,b,c,etc.)
    signals = data["Signal"].unique()

    #creating a subplot for each variable ( each variable has its own wave) + aligns it
    fig, ax = plt.subplots(len(signals), 1, figsize=(10, 2 * len(signals)), sharex=True)

    # plotting each variable on its subplot
    for i, signal in enumerate(signals):
        signal_data = data[data["Signal"] == signal]

        # keeps the value of the variable until next change
        ax[i].step(signal_data["Time"], signal_data["Value"], where="post", label=signal, color="blue")
        
        
        ax[i].set_ylim(-0.5, 1.5)
        ax[i].set_yticks([0, 1]) # ensuring it's only 0's and 1'ss
        ax[i].set_ylabel(signal)
        ax[i].legend(loc="upper right")
        
    # setting up the names
    ax[-1].set_xlabel("Time (ps)")
    plt.suptitle("simulation waveforms")
    plt.show()

simulation_file = "circuit_output.sim"
plot_waveform(simulation_file) # to plot the output.sim 