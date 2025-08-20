from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.histogram import plot_histogram
import os
import numpy as np
from src.plots.box import plot_boxplots_from_csv
import matplotlib as mpl


def plot_paschen(df, save_path):
    gaps = df["gap_fixed"].unique().tolist()
    cmap = plt.get_cmap("tab20")  # or "tab20" if you have many gaps
    colors = mpl.cm.get_cmap(cmap, len(gaps))  # distinct colors
    fig, ax = thesis_figure()
    for i, gap in enumerate(gaps):
        df_plot = df[df["gap_fixed"] == gap].copy()

        ax.scatter(
            df_plot["pd"], df_plot["voltage"], label=f"{gap} cm", color=colors(i), s=0.1
        )

        ax.set_title("pd gegen Spannung")

        ax.set_xlabel("pd in mbar$\cdot$cm")
        ax.set_xlabel("Spannung U in kV")

        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), title="Gap size")

    # Adjust layout and save
    fig.tight_layout()
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/classes"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/classes"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    # plot paschen electrodes
    df = pd.read_csv(CSV_PATH + "/paschen_electrodes.csv")
    plot_paschen(df, FIGURES_PATH + "/paschen_electrodes.pdf")

    df = pd.read_csv(CSV_PATH + "/paschen_plates.csv")
    plot_paschen(df, FIGURES_PATH + "/paschen_plates.pdf")
