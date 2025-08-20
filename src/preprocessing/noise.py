from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from src.plots.discharge_plot import plot_discharge
from dotenv import load_dotenv
import os
import numpy as np


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    plot_discharge(
        csv_file=CSV_PATH + "/discharge_noise.csv",
        column="current",
        title="Aufnahme mit Rauschen",
        xlabel="Zeit t in s",
        ylabel="Strom in A",
        save_path=FIGURES_PATH + "/discharge_noise.pdf",
    )
