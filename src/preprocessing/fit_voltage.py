from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import numpy as np


def formula(x):
    return 1.509 * x - 1.236


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/fit_voltage_data.csv")

    fig, ax = thesis_figure()
    ax.scatter(df["input_voltage"], df["measured_voltage"], label="Messpunkte")

    x = np.linspace(df["input_voltage"].min(), df["input_voltage"].max(), 100)

    y = [formula(y) for y in x]

    ax.plot(x, y, "r--", label="Fit mit y = $1,509 \\cdot x - 1,236$")

    # Set axis labels and title
    ax.set_xlabel("Spannung $U_{netz}$ am Netzteil")
    ax.set_ylabel("Ausgangspannung $U_{aus}$")
    ax.set_title("$U_{netz}$ vs $U_{aus}$")

    # Adjust layout and save
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES_PATH + "/fit_voltage_data.pdf")
    print("Saved figure")
