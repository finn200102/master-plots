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


def plot_rise(figure_name, df):
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
    pd.set_option("display.precision", 12)

    t_fit = start_part["Time"] - df["event_start"].iloc[0]

    fitted_values = t_fit.apply(
        lambda t: discharge_rise(t, df["a"].iloc[0], df["tau"].iloc[0], df["c"].iloc[0])
    )

    ax.plot(start_part["Time"], fitted_values, label="Fit", color="red")

    ax.set_title("Strom gegen die Zeit")
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    ax.set_xlim(df["event_start"].iloc[0] - 1e-7, df["event_start"].iloc[0] + 1e-7)
    fig.tight_layout()
    save_path = FIGURES_PATH + f"/{figure_name}.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")

    plt.close(fig)


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/discharge_rise_time.csv")

    plot_rise(figure_name="/discharge_rise_time", df=df)

    df = pd.read_csv(CSV_PATH + "/discharge_rise_time_0p9.csv")

    plot_rise(figure_name="/discharge_rise_time_0p9", df=df)

    df = pd.read_csv(CSV_PATH + "/discharge_rise_time_0p8.csv")

    plot_rise(figure_name="/discharge_rise_time_0p8", df=df)

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
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="a_rise_histo.pdf",
        csv_name="taus_rise",
        column="a",
        title="Verteilung der a",
        xlabel="a",
        ylabel="Anzahl",
        nbins=50,
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="c_rise_histo.pdf",
        csv_name="taus_rise",
        column="c",
        title="Verteilung der c",
        xlabel="c",
        ylabel="Anzahl",
        nbins=50,
    )

    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="score_rise_histo.pdf",
        csv_name="taus_rise",
        column="score",
        title="Verteilung der score",
        xlabel="score",
        ylabel="Anzahl",
        nbins=100,
    )

    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="score_rise_histo_zoom.pdf",
        csv_name="taus_rise",
        column="score",
        title="Verteilung der score",
        xlabel="score",
        ylabel="Anzahl",
        xlim=0.5,
        nbins=1000,
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

    # taus vs score
    #
    fig, ax = thesis_figure()
    df = pd.read_csv(CSV_PATH + "/taus_rise.csv")
    ax.scatter(df["score"], df["tau"])
    ax.set_title("Taus vs score")
    ax.set_xlabel("score")
    ax.set_ylabel("taus in s")
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.tight_layout()
    save_path = FIGURES_PATH + "/taus_rise_score_scatter.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")

    plt.close(fig)
