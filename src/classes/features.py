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
        title="Spaltabstand vs Ladung",
        xlabel="Spaltabstand d in cm",
        ylabel="Ladung Q in C",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_charge_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_charge",
        title="Spaltabstand vs Ladung",
        xlabel="Spaltabstand d in cm",
        ylabel="Ladung Q in C",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_plates_gap.pdf",
    )
    """
    plot_boxplots_from_csv(
        CSV_PATH + "/event_charge_box_electrodes.csv",
        x_col="pd",
        y_col="event_charge",
        num_bins=5,
        title="pd vs Ladung",
        xlabel="pd in mbar cm",
        ylabel="Ladung Q in C",
        y_scale="log",
        save_path=FIGURES_PATH + "/event_charge_box_electrodes_pd.pdf",
    )
    """
    # event_distance
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_distance",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_distance_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_distance",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_distance_box_plates_gap.pdf",
    )
    # event_duration
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_duration_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_duration",
        title="Spaltabstand vs Eventlänge",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventlänge in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_duration_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_duration_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_duration",
        title="Spaltabstand vs Eventlänge",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventlänge in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_duration_box_plates_gap.pdf",
    )
    # event_energy
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_energy_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="event_energy",
        title="Spaltabstand vs Eventenergie",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventenergie J",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_energy_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/event_energy_box_plates.csv",
        x_col="gap_fixed",
        y_col="event_energy",
        title="Spaltabstand vs Eventenergie",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventenergie in J",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/event_energy_box_plates_gap.pdf",
    )
    # max_current
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/max_current_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="max_current",
        title="Spaltabstand vs maximaler Strom",
        xlabel="Spaltabstand d in cm",
        ylabel="maximaler Strom $I_{max}$ in A",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/max_current_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/max_current_box_plates.csv",
        x_col="gap_fixed",
        y_col="max_current",
        title="Spaltabstand vs maximaler Strom",
        xlabel="Spaltabstand d in cm",
        ylabel="maximaler Strom $I_{max}$ in A",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/max_current_box_plates_gap.pdf",
    )
    # precursor_distance
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="precursor_distance",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_box_electrodes_gap.pdf",
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
        save_path=FIGURES_PATH + "/precursor_distance_box_plates_gap.pdf",
    )
    # precursor_distance_manual
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/precursor_distance_manual_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="precursor_distance_manual",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/precursor_distance_manual_box_electrodes_gap.pdf",
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
        save_path=FIGURES_PATH + "/precursor_distance_manual_box_plates_gap.pdf",
    )
    # voltage
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/voltage_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="voltage",
        title="Spaltabstand vs Durchbruchspannung",
        xlabel="Spaltabstand d in cm",
        ylabel="Durchbruchspannung $U_{break}$ in kV",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/voltage_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/voltage_box_plates.csv",
        x_col="gap_fixed",
        y_col="voltage",
        title="Spaltabstand vs Durchbruchspannung",
        xlabel="Spaltabstand d in cm",
        ylabel="Durchbruchspannung $U_{break}$ in kV",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/voltage_box_plates_gap.pdf",
    )

    # voltage_drop
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/voltage_drop_box_electrodes.csv",
        x_col="gap_fixed",
        y_col="voltage_drop",
        title="Spaltabstand vs Spannungsabfall",
        xlabel="Spaltabstand d in cm",
        ylabel="Spannungsabfall $U_{diff}$ in kV",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/voltage_drop_box_electrodes_gap.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/voltage_drop_box_plates.csv",
        x_col="gap_fixed",
        y_col="voltage_drop",
        title="Spaltabstand vs Spannungsabfall",
        xlabel="Spaltabstand d in cm",
        ylabel="Spannungsabfall $U_{diff}$ in kV",
        sort_classes=True,
        y_scale="log",
        save_path=FIGURES_PATH + "/voltage_drop_box_plates_gap.pdf",
    )
