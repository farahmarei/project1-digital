#
import matplotlib.pyplot as plt
import pandas as pd

def plot_waveform(simulation_file):
    # Load the simulation output file into a DataFrame
    data = pd.read_csv(simulation_file, header=None, names=["Time", "Signal", "Value"])

    # Get unique signals
    signals = data["Signal"].unique()
    fig, ax = plt.subplots(len(signals), 1, figsize=(10, 2 * len(signals)), sharex=True)

    # Plot each signal on its own subplot
    for i, signal in enumerate(signals):
        # Filter data for the current signal
        signal_data = data[data["Signal"] == signal]

        # Plot signal waveform using step to keep values until next change
        ax[i].step(signal_data["Time"], signal_data["Value"], where="post", label=signal, color="blue")
        
        # Set labels and limits
        ax[i].set_ylim(-0.5, 1.5)
        ax[i].set_yticks([0, 1])
        ax[i].set_ylabel(signal)
        ax[i].legend(loc="upper right")
        
    ax[-1].set_xlabel("Time (ps)")
    plt.suptitle("Simulation Waveforms")
    plt.show()

simulation_file = "circuit_output.sim"
plot_waveform(simulation_file)