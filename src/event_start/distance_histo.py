from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from src.plots.histogram import plot_histogram
import os
import numpy as np


def plot_log_histo(
    FIGURES_PATH,
    CSV_PATH,
    csv_name,
    column,
    xlabel,
    ylabel,
    title,
    figures_name,
    nbins=25,
):
    import os
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # 1) Load
    f = os.path.join(CSV_PATH, f"{csv_name}.csv")
    df = pd.read_csv(f)

    vals = pd.to_numeric(df[column], errors="coerce").to_numpy()
    # Remove NaNs and non-positives for log scale
    vals = vals[np.isfinite(vals) & (vals > 0)]
    if vals.size == 0:
        print(f"[plot_log_histo] No positive finite values in column '{column}'.")
        return

    # 2) Bin edges on a valid positive log range
    lo, hi = float(vals.min()), float(vals.max())

    if lo == hi:
        # Expand a touch around a single value so logspace has breadth
        lo *= 0.9
        hi *= 1.1
        # If the single value is extremely small, enforce a tiny positive floor
        if lo <= 0:
            lo = max(hi * 0.5, 1e-12)

    # Safety: ensure lo < hi and strictly increasing bins
    if not (lo > 0 and hi > lo):
        # last resort: define a narrow decade around hi
        lo = max(hi / 10.0, 1e-12)

    bins = np.logspace(np.log10(lo), np.log10(hi), nbins + 1)

    # 3) Histogram
    freqs, edges = np.histogram(vals, bins=bins)
    bin_centres = np.sqrt(edges[:-1] * edges[1:])  # geometric mean

    # 4) Plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(
        bin_centres,
        freqs,
        width=np.diff(bins),
        align="center",
        edgecolor="black",
        linewidth=0.5,
        alpha=0.85,
        color="#4682B4",
    )
    ax.set_xscale("log")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    fig.tight_layout()

    out_f = os.path.join(FIGURES_PATH, figures_name)
    fig.savefig(out_f)
    plt.close(fig)


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/event_start"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="event_distance.pdf",
        csv_name="event_distance",
        column="event_distance",
        title="Verteilung der Eventabstände",
        xlabel="Eventabstand",
        ylabel="Anzahl",
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="event_distance_hand.pdf",
        csv_name="event_distance_manual",
        column="event_distance_manual",
        title="Verteilung der Eventabstände händisch",
        xlabel="Eventabstand",
        ylabel="Anzahl",
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="precursor_distance.pdf",
        csv_name="precursor_distance",
        column="precursor_distance",
        title="Verteilung der Vorläuferabstände",
        xlabel="Vorläuferabstand",
        ylabel="Anzahl",
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="precursor_distance_hand.pdf",
        csv_name="precursor_distance_manual",
        column="precursor_distance_manual",
        title="Verteilung der Vorläuferabstände händisch",
        xlabel="Vorläuferabstand",
        ylabel="Anzahl",
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="precursor_distance_all.pdf",
        csv_name="precursor_distance_all",
        column="precursor_distance",
        title="Verteilung der Vorläuferabstände",
        xlabel="Vorläuferabstand",
        ylabel="Anzahl",
    )
    plot_log_histo(
        CSV_PATH=CSV_PATH,
        FIGURES_PATH=FIGURES_PATH,
        figures_name="precursor_distance_hand_all.pdf",
        csv_name="precursor_distance_manual_all",
        column="precursor_distance_manual",
        title="Verteilung der Vorläuferabstände händisch",
        xlabel="Vorläuferabstand",
        ylabel="Anzahl",
    )
