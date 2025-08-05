from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from src.plots.histogram import plot_histogram


if __name__ == "__main__":
    # Electrode setup
    plot_histogram(
        csv_file="setup_histo.csv",
        column="electrode",
        bins=[0.5, 1.5, 2.5],
        title="Anteil der beiden Elektroden",
        xlabel="Elektroden Typ",
        ylabel="Anzahl",
        xticks=[1, 2],
        xticklabels=["Stab", "Platte"],
    )
    plot_histogram(
        csv_file="channel_histo.csv",
        column="channel",
        bins=[0.5, 1.5, 2.5, 3.5, 4.5],
        title="Anteil der 4 Kanäle",
        xlabel="Kanäle",
        ylabel="Anzahl",
        xticks=[1, 2, 3, 4],
        xticklabels=["Kanal 1", "Kanal 2", "Kanal 3", "Kanal 4"],
    )
