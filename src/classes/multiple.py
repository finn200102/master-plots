from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.histogram import plot_histogram

from matplotlib import cm, colors
import os
import numpy as np


def discharge_curve(t, A, tau):
    return A * np.exp(-t / tau)


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/classes"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/classes/"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/discharge_multiple.csv")

    fig, ax = thesis_figure()

    ax.plot(df["Time"], df["current"])

    taus = []
    onsets = []

    for idx in range(len(df.filter(like="onest", axis=1).columns)):
        onset = df[f"onest_{idx:02d}"].iloc[0]
        a = df[f"ass_{idx:02d}"].iloc[0]

        onsets.append(onset)
        t = df[f"tau_{idx:02d}"].iloc[0]
        taus.append(t)

        ax.axvline(df["Time"][onset], color="red")

        if idx > 0:
            start = df["Time"][onsets[-2]]  # - 9e-5
            end = df["Time"][onset] - 2e-5

            print(start)
            print(end)

            part = df[
                (df["Time"] > start) & (df["Time"] < end)
            ].copy()  # avoid SettingWithCopy

            t_shifted = part["Time"].to_numpy() - part["Time"].iloc[0]
            part["target"] = discharge_curve(t_shifted, a, t)

            ax.plot(part["Time"], part["target"])

    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")

    fig.tight_layout()
    save_path = FIGURES_PATH + "/discharge_multiple.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)

    # save histogram for taus

    fig, ax = thesis_figure()

    mu = np.array(taus).mean()
    median = np.median(np.array(taus))
    sigma = np.array(taus).std()
    textstr = "\n".join(
        (
            rf"$\mu={mu:.3e}$",
            rf"$\mathrm{{median}}={median:.3e}$",
            rf"$\sigma={sigma:.3e}$",
        )
    )
    props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

    taus_flat = np.concatenate([np.asarray(t).ravel() for t in taus])
    counts, bins, patches = ax.hist(taus_flat, bins=30, edgecolor="black")

    norm = colors.Normalize(vmin=bins.min(), vmax=bins.max())
    for patch, l, r in zip(patches, bins[:-1], bins[1:]):
        color = cm.RdYlGn_r(norm((l + r) / 2))
        patch.set_facecolor(color)

    # place a text box in upper left in axes coords
    ax.text(
        0.05,
        0.95,
        textstr,
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment="top",
        bbox=props,
    )

    ax.set_title("Histogram der taus")
    ax.set_xlabel("Taus in s")
    ax.set_ylabel("Anzahl")
    save_path = FIGURES_PATH + "/multiple_tau_histo.pdf"
    fig.savefig(save_path)
    plt.close(fig)
