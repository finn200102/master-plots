from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.histogram import plot_histogram
import os
import numpy as np
from src.plots.box import plot_boxplots_from_csv_classes, plot_boxplots_from_csv

if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/classes"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/classes/"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    # charge
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_charge_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_charge",
        title="Price by City",
        xlabel="City",
        ylabel="Price",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_electrodes_gsp.pdf",
    )
    plot_boxplots_from_csv(
        CSV_PATH + "/event_charge_box_electrodes.csv",
        x_col="pd",
        y_col="event_charge",
        num_bins=5,
        title="pd vs Ladung",
        xlabel="pd",
        ylabel="Ladung",
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_electrodes_pd.pdf",
    )
    plot_boxplots_from_csv(
        CSV_PATH + "/event_charge_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_charge",
        num_bins=5,
        title="Spaltabstand vs Ladung",
        xlabel="Spaltabstand",
        ylabel="Ladung",
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_electrodes_gap.pdf",
    )
