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

    df = pd.read_csv(CSV_PATH + "/fix_pressure.csv")

    # for each pressure interal
    gaps = df["gap"].values.tolist()
    gaps = sorted(list(set(gaps)))
    print(gaps)

    for idx, gap in enumerate(gaps):
        df_g = df[df["gap"] == gap]

        fig, ax = thesis_figure()
        df_g_fixed = df_g[df["pressure"].isnull()]
        ax.scatter(
            df_g["voltage"],
            df_g["pressure"],
            label="Messpunkte",
        )
        ax.scatter(df_g_fixed["voltage"], df_g_fixed["pressure_fixed"], label="Fixed")

        # Set axis labels and title
        ax.set_xlabel("Spannung $U_{netz}$ am Netzteil")
        ax.set_ylabel("Druck p in mbar")
        ax.set_title("Spannung gegen Druck")

        # Adjust layout and save
        ax.legend(loc="upper left")
        fig.tight_layout()
        fig.savefig(FIGURES_PATH + f"/fix_pressure__gap{gap}.pdf")
        print("Saved figure")
