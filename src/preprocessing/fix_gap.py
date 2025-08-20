from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import numpy as np


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/preprocessing"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/fix_gap.csv")

    # for each pressure interal
    pressures = df["pressure"].values.tolist()
    pressures = [round(p) for p in pressures]
    pressures = sorted(list(set(pressures)))
    print(pressures)

    for idx, pressure in enumerate(pressures):
        if idx > 0:
            df_p = df[
                (df["pressure"] <= pressure) & (df["pressure"] > pressures[idx - 1])
            ]
        else:
            df_p = df[df["pressure"] <= pressure]

        fig, ax = thesis_figure()
        df_p_fixed = df_p[df["gap"].isnull()]
        ax.scatter(df_p["voltage"], df_p["gap"], label="Messpunkte")
        ax.scatter(df_p_fixed["voltage"], df_p_fixed["gap_fixed"], label="Fixed")

        # Set axis labels and title
        ax.set_xlabel("Spannung $U_{netz}$ am Netzteil")
        ax.set_ylabel("Spaltabstand d")
        ax.set_title("Spannung gegen Spaltabstand")

        # Adjust layout and save
        ax.legend(loc="upper left")
        fig.tight_layout()
        fig.savefig(FIGURES_PATH + f"/fix_gap__pressure{pressure}.pdf")

        print("Saved figure")
