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

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/event_start/"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    # event_distance_box_plates.csv
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_distance",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_box_plates.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_distance",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_box_electrodes.pdf",
    )

    # Precursor distance
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="precursor_distance",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_box_electrodes.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_box_plates.csv",
        x_col="gap_fixed",
        y_col="precursor_distance",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_box_plates.pdf",
    )
    # precursor distance manual
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_manual_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="precursor_distance_manual",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_manual_box_electrodes.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_manual_box_plates.csv",
        x_col="gap_fixed",
        y_col="precursor_distance_manual",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_manual_box_plates.pdf",
    )

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_manual_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_distance_manual",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_manual_box_plates.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_manual_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_distance_manual",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_manual_box_electrodes.pdf",
    )

    # event distance manual
"""
event_distance.csv
event_distance_box_electrodes.csv
event_distance_box_plates.csv
event_distance_manual.csv
event_distance_manual_box_electrodes.csv
event_distance_manual_box_plates.csv
precursor_distance.csv
precursor_distance_box_electrodes.csv
precursor_distance_box_plates.csv
precursor_distance_manual.csv
precursor_distance_manual_box_electrodes.csv
precursor_distance_manual_box_plates.csv
"""
