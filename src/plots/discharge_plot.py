from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_discharge(
    csv_file,
    column,
    title,
    xlabel,
    ylabel,
    x_lim=None,
    y_lim=None,
    save_path="plot.pdf",
):
    """
    Plot a plot for a discharges df.
    """

    df = pd.read_csv(csv_file)

    fig, ax = thesis_figure()
    ax.plot(df["Time"], df[column])

    # Set axis labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Set lims
    if x_lim is not None:
        ax.set_xlim(x_lim)
    if y_lim is not None:
        ax.set_ylim(y_lim)

    # Adjust layout and save
    fig.tight_layout()
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)
