from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from src.plots.discharge_plot import plot_discharge
from src.plots.histogram import plot_histogram
from src.event_start.distance_histo import plot_log_histo
from src.plots.box import plot_boxplots_from_csv_classes
from dotenv import load_dotenv
import os
import numpy as np


def discharge_rise(t, A, tau, C):
    # return A * (1 - np.exp(-t / tau)) + C
    return A * np.exp(t / tau) + C


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/discharge_rise_time.csv")

    fig, ax = thesis_figure()

    ax.plot(df["Time"], df["current"], label="Plot")

    start_window = df[
        (df["Time"] < df["event_start"].iloc[0] + 1e-9)
        & (df["Time"] > df["event_start"].iloc[0] - 1e-7)
    ]

    # Step 2: Find the time of the max Channel_1 value within this window
    max_time = start_window.loc[start_window["current"].idxmax(), "Time"]

    # Step 3: Slice from the start of the window to the time of the maximum Channel_1
    start_part = df[
        (df["Time"] >= df["event_start"].iloc[0] - 5e-8) & (df["Time"] <= max_time)
    ]

    fitted_values = start_part["Time"].apply(
        lambda t: discharge_rise(t, df["a"].iloc[0], df["tau"].iloc[0], df["c"].iloc[0])
    )
    ax.plot(start_part["Time"], fitted_values, label="Fit")

    ax.set_title("Strom gegen die Zeit")
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    fig.tight_layout()
    save_path = FIGURES_PATH + "/discharge_rise_time.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")

    plt.close(fig)

    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="taus_rise_histo.pdf",
        csv_name="taus_rise",
        column="tau",
        title="Verteilung der taus",
        xlabel="taus in s",
        ylabel="Anzahl",
        nbins=50,
    )

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/taus_rise.csv",
        x_col="gap",
        y_col="tau",
        title="Spaltabstand vs taus",
        xlabel="Spaltabstand d in cm",
        ylabel="taus in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/taus_rise_box.pdf",
    )
