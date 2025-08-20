from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.histogram import plot_histogram
import os
import numpy as np


def plot_histo_pressures(FIGURES_PATH, CSV_PATH, csv_name, column):
    df = pd.read_csv(os.path.join(CSV_PATH, f"{csv_name}.csv"))

    # Round to 0.1 consistently
    pressures_rounded = np.round(df[column].astype(float).to_numpy(), 1)

    # Count per unique value and sort by the bin (x) value
    counts = pd.Series(pressures_rounded).value_counts().sort_index()
    values = counts.index.to_numpy()
    freqs = counts.values

    # Bin width ~ 90% of the minimum spacing (or a default if only one bin)
    bin_width = (np.min(np.diff(values)) * 0.9) if len(values) > 1 else 0.1

    # Color by the bin value thresholds
    colors = [("#d62728" if (v >= 7) or (v <= 0.1) else "#4682B4") for v in values]

    fig, ax = plt.subplots()
    ax.bar(
        values,
        freqs,
        width=bin_width,
        align="center",
        edgecolor="black",
        linewidth=0.5,
        alpha=0.85,
        color=colors,
    )

    ax.set_xlabel("Drücke")
    ax.set_ylabel("Anzahl")
    ax.set_title("Anteil der Drücke")

    fig.tight_layout()
    out_path = os.path.join(FIGURES_PATH, f"{csv_name}.pdf")
    fig.savefig(out_path)
    print(f"Saved figure to {out_path}")
    plt.close(fig)


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/overview"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/overview/"

    os.makedirs(FIGURES_PATH, exist_ok=True)
    # Electrode setup
    plot_histogram(
        csv_file=CSV_PATH + "setup_histo.csv",
        column="electrode",
        bins=[0.5, 1.5, 2.5],
        title="Anteil der beiden Elektroden",
        xlabel="Elektroden Typ",
        ylabel="Anzahl",
        xticks=[1, 2],
        xticklabels=["Stab", "Platte"],
        save_path=FIGURES_PATH + "/setup_histo.pdf",
    )
    plot_histogram(
        csv_file=CSV_PATH + "channels_histo.csv",
        column="channel",
        bins=[0.5, 1.5, 2.5, 3.5, 4.5],
        title="Anteil der 4 Kanäle",
        xlabel="Kanäle",
        ylabel="Anzahl",
        xticks=[1, 2, 3, 4],
        xticklabels=["Kanal 1", "Kanal 2", "Kanal 3", "Kanal 4"],
        save_path=FIGURES_PATH + "/channels_histo.pdf",
    )
    plot_histogram(
        csv_file=CSV_PATH + "gaps_electrodes_histo.csv",
        column="electrode",
        bins=10,
        title="Anteil der Spaltabstände",
        xlabel="Spaltabstände",
        ylabel="Anzahl",
        save_path=FIGURES_PATH + "/gaps_electrodes_histo.pdf",
    )
    plot_histogram(
        csv_file=CSV_PATH + "gaps_plates_histo.csv",
        column="plates",
        bins=10,
        title="Anteil der Spaltabstände",
        xlabel="Spaltabstände",
        ylabel="Anzahl",
        save_path=FIGURES_PATH + "/gaps_plates_histo.pdf",
    )
    plot_histogram(
        csv_file=CSV_PATH + "timelens_electrodes_histo.csv",
        column="electrode",
        bins=10,
        title="Anteil der zeitlichen Messbereiche",
        xlabel="zeitlicher Messbereich",
        ylabel="Anzahl",
        save_path=FIGURES_PATH + "/timelens_electrodes_histo.pdf",
    )
    plot_histogram(
        csv_file=CSV_PATH + "timelens_plates_histo.csv",
        column="plates",
        bins=10,
        title="Anteil der zeitlichen Messbereiche",
        xlabel="zeitlicher Messbereich",
        ylabel="Anzahl",
        save_path=FIGURES_PATH + "/timelens_plates_histo.pdf",
    )

    plot_histo_pressures(
        FIGURES_PATH, CSV_PATH, "pressure_electrodes_histo", "electrode"
    )

    plot_histo_pressures(FIGURES_PATH, CSV_PATH, "pressure_plates_histo", "plates")
