from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt
from src.plots.discharge_plot import plot_discharge
from dotenv import load_dotenv
import os
import numpy as np


if __name__ == "__main__":
    load_dotenv()

    FIGURES_PATH = os.getenv("FIGURES_PATH") + "/features"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    CSV_PATH = os.getenv("CSV_PATH") + "/features"

    os.makedirs(FIGURES_PATH, exist_ok=True)

    df = pd.read_csv(CSV_PATH + "/event_markers.csv")

    # precursor_markers
    fig, ax = thesis_figure()
    ax.plot(df["Time"], df["current"])

    ax.axvline(
        x=df["precursor_start"].iloc[0],
        color="black",
        linestyle="--",
        linewidth=0.5,
        label="Vorläuferstart",
    )
    ax.axvline(
        x=df["precursor_end"].iloc[0],
        color="brown",
        linestyle="--",
        linewidth=0.5,
        label="Vorläuferend",
    )
    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    ax.set_title("Strom vs Zeit")

    ax.set_xlim(df["precursor_start"].iloc[0] - 1e-6, df["event_start"].iloc[0])
    # ax.set_ylim(y_lim)

    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    # Adjust layout and save
    fig.tight_layout()
    save_path = FIGURES_PATH + "/precursor_markers.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)

    # precursor_markers_hand
    fig, ax = thesis_figure()
    ax.plot(df["Time"], df["current"])

    ax.axvline(
        x=df["precursor_start_hand"].iloc[0],
        color="black",
        linestyle="--",
        linewidth=0.5,
        label="Vorläuferstart",
    )
    ax.axvline(
        x=df["precursor_end_hand"].iloc[0],
        color="brown",
        linestyle="--",
        linewidth=0.5,
        label="Vorläuferend",
    )
    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    ax.set_title("Strom vs Zeit")

    ax.set_xlim(df["precursor_start_hand"].iloc[0] - 1e-6, df["event_start"].iloc[0])
    # ax.set_ylim(y_lim)

    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    # Adjust layout and save
    fig.tight_layout()
    save_path = FIGURES_PATH + "/precursor_markers_hand.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)

    # event markers
    fig, ax = thesis_figure()
    ax.plot(df["Time"], df["current"])

    ax.axvline(
        x=df["event_start"].iloc[0],
        color="black",
        linestyle="--",
        linewidth=0.5,
        label="Eventstart",
    )
    ax.axvline(
        x=df["event_end"].iloc[0],
        color="brown",
        linestyle="--",
        linewidth=0.5,
        label="Eventende",
    )
    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    ax.set_title("Strom vs Zeit")

    ax.set_xlim(df["precursor_start"].iloc[0] - 1e-6)
    # ax.set_ylim(y_lim)

    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    # Adjust layout and save
    fig.tight_layout()
    save_path = FIGURES_PATH + "/event_markers.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)

    # event markers_hand
    fig, ax = thesis_figure()
    ax.plot(df["Time"], df["current"])

    ax.axvline(
        x=df["event_start_hand"].iloc[0],
        color="black",
        linestyle="--",
        linewidth=0.5,
        label="Eventstart",
    )
    ax.axvline(
        x=df["event_end_hand"].iloc[0],
        color="brown",
        linestyle="--",
        linewidth=0.5,
        label="Eventende",
    )
    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")
    ax.set_title("Strom vs Zeit")

    ax.set_xlim(df["precursor_start_hand"].iloc[0] - 1e-6)
    # ax.set_ylim(y_lim)

    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    # Adjust layout and save
    fig.tight_layout()
    save_path = FIGURES_PATH + "/event_markers_hand.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)

    # max_current, voltage, voltage_drop
    fig, ax = thesis_figure()
    # Strom
    ax.plot(df["Time"], df["current"], label="Strom")
    # max current
    ax.axhline(df["max_current"].iloc[0], color="blue", ls=":")
    ax.text(
        -0.05,  # left side (a bit outside)
        df["max_current"].iloc[0],
        f"{df['max_current'].iloc[0]:.2f}",
        color="blue",
        va="center",
        ha="right",  # align text to the right edge
        transform=ax.get_yaxis_transform(),
    )

    ax2 = ax.twinx()
    ax2.plot(df["Time"], df["voltage"], "r--", label="Spannung")

    ax2.axhline(df["voltage_start"].iloc[0], color="red", ls=":")
    ax2.text(
        1.01,
        df["voltage_start"].iloc[0],
        f"{df['voltage_start'].iloc[0]:.2f}",
        color="red",
        va="center",
        ha="left",
        transform=ax2.get_yaxis_transform(),
    )
    voltage_drop = df["voltage_start"].iloc[0] - df["voltage_drop"].iloc[0]
    ax2.axhline(voltage_drop, color="red", ls=":")
    ax2.text(
        1.01,
        voltage_drop,
        f"{voltage_drop:.2f}",
        color="red",
        va="center",
        ha="left",
        transform=ax2.get_yaxis_transform(),
    )

    # Set axis labels and title
    ax.set_xlabel("Zeit t in s")
    ax.set_ylabel("Strom in A")

    ax2.set_ylabel("Spannung in kV")
    ax.set_title("Strom vs Zeit")

    # ax.set_ylim(y_lim)

    # Collect handles & labels from both axes
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    # Put them together
    ax.legend(
        lines1 + lines2, labels1 + labels2, loc="lower right", frameon=True
    )  # puts legend inside bottom right
    # Adjust layout and save
    fig.tight_layout()
    save_path = FIGURES_PATH + "/event_voltage_current.pdf"
    fig.savefig(save_path)
    print(f"Saved figure to {save_path}")
    plt.close(fig)
