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

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/maschinelearning"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/maschinelearning"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/features_prec_ts_df.csv")
    fig, ax = thesis_figure()
    df["0_Time"] = df["0_Time"] - df["0_Time"].iloc[0]
    df["1_Time"] = df["1_Time"] - df["1_Time"].iloc[0]
    df["2_Time"] = df["2_Time"] - df["2_Time"].iloc[0]
    ax.plot(df["0_Time"], df["0_current"])
    ax.plot(df["1_Time"], df["1_current"])
    ax.plot(df["2_Time"], df["2_current"])
    ax.set_title("Entladestrom gegen die Zeit")
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom I in A")

    fig.tight_layout()
    fig.savefig(FIGURES_PATH + "/features_prec_ts_df.pdf")
    plt.close(fig)

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/features_prec_ts_event_distance_histo.csv",
        x_col="gap_fixed",
        y_col="event_distance",
        title="Spaltabstand vs Eventabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventabstand in s",
        sort_classes=True,
        save_path=FIGURES_PATH + "/features_prec_ts_event_distance_box.pdf",
    )
    plot_boxplots_from_csv_classes(
        CSV_PATH + "/features_prec_ts_precursor_distance_histo.csv",
        x_col="gap_fixed",
        y_col="precursor_distance",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        save_path=FIGURES_PATH + "/features_prec_ts_precursor_distance_box.pdf",
    )

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/features_prec_ts_event_duration_histo.csv",
        x_col="gap_fixed",
        y_col="event_duration",
        title="Spaltabstand vs Eventlänge",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventlänge in s",
        sort_classes=True,
        save_path=FIGURES_PATH + "/features_prec_ts_event_duration_box.pdf",
    )

    df = pd.read_csv(CSV_PATH + "/features_streamer_hand_df.csv")
    fig, ax = thesis_figure()
    df["0_Time"] = df["0_Time"] - df["0_Time"].iloc[0]
    df["1_Time"] = df["1_Time"] - df["1_Time"].iloc[0]
    df["2_Time"] = df["2_Time"] - df["2_Time"].iloc[0]
    ax.plot(df["0_Time"], df["0_current"])
    ax.plot(df["1_Time"], df["1_current"])
    ax.plot(df["2_Time"], df["2_current"])
    ax.set_title("Entladestrom gegen die Zeit")
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom I in A")

    fig.tight_layout()
    fig.savefig(FIGURES_PATH + "/features_streamer_hand_df.pdf")
    plt.close(fig)

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/features_streamer_hand_precursor_distance_histo.csv",
        x_col="gap_fixed",
        y_col="precursor_distance",
        title="Spaltabstand vs Vorläuferabstand",
        xlabel="Spaltabstand d in cm",
        ylabel="Vorläuferabstand in s",
        sort_classes=True,
        save_path=FIGURES_PATH + "/features_streamer_hand_precursor_distance_box.pdf",
    )

    plot_boxplots_from_csv_classes(
        CSV_PATH + "/features_streamer_hand_event_duration_histo.csv",
        x_col="gap_fixed",
        y_col="event_duration",
        title="Spaltabstand vs Eventlänge",
        xlabel="Spaltabstand d in cm",
        ylabel="Eventlänge in s",
        sort_classes=True,
        save_path=FIGURES_PATH + "/features_streamer_hand_event_duration_box.pdf",
    )
