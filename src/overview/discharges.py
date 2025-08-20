from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.discharge_plot import plot_discharge
import os

if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/overview"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/overview/"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    plot_discharge(
        csv_file=CSV_PATH + "discharge_multiple.csv",
        column="current",
        title="Aufnahme mit mehreren Entladungen",
        xlabel="Zeit t in s",
        ylabel="Strom in A",
        save_path=FIGURES_PATH + "/discharge_multiple.pdf",
    )
    plot_discharge(
        csv_file=CSV_PATH + "discharge_constend.csv",
        column="current",
        title="Aufnahme mit hoher Aufösung des Stroms",
        xlabel="Zeit t in s",
        ylabel="Strom in A",
        save_path=FIGURES_PATH + "/discharge_constend.pdf",
    )
    plot_discharge(
        csv_file=CSV_PATH + "discharge_makro.csv",
        column="current",
        title="Aufnahme mit niedriger zeitlicher Aufösung",
        xlabel="Zeit t in s",
        ylabel="Strom in A",
        save_path=FIGURES_PATH + "/discharge_makro.pdf",
        y_lim=(-0.0003, 0.0003),
    )
    plot_discharge(
        csv_file=CSV_PATH + "discharge_mikro.csv",
        column="current",
        title="Aufnahme mit hoher zeitlicher Aufösung",
        xlabel="Zeit t in s",
        ylabel="Strom in A",
        save_path=FIGURES_PATH + "/discharge_mikro.pdf",
        y_lim=(-0.0003, 0.0003),
    )
