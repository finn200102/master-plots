import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Iterable, Optional, Sequence, Union

Number = Union[int, float, np.number]


def _decimals(w: float) -> int:
    """Heuristic for nice decimal places in bin labels."""
    if w == 0:
        return 2
    p = max(0, int(np.ceil(-np.log10(w))) + 1)
    return min(p, 6)


def plot_boxplots_from_csv(
    csv_file: str,
    x_col: str,
    y_col: str,
    num_bins: int,
    title: str,
    xlabel: str,
    ylabel: str,
    y_scale: str = "linear",  # "linear" or "log"
    save_path: str = "boxplot.pdf",
    showfliers: bool = True,
):
    """
    Create boxplots of y-values grouped into `num_bins` equal-width bins of x-values.

    Parameters
    ----------
    csv_file : str
        Path to the CSV file.
    x_col : str
        Column name for x-values.
    y_col : str
        Column name for y-values.
    num_bins : int
        Number of equal-width bins along x (=> number of boxplots).
    title, xlabel, ylabel : str
        Plot text.
    y_scale : {"linear","log"}
        Y-axis scale. If "log", non-positive y values are dropped (with a warning).
    save_path : str
        Where to save the figure.
    showfliers : bool
        Show outliers in the boxplot.
    """

    # Load and clean
    df = pd.read_csv(csv_file)
    df = df.dropna(subset=[x_col, y_col])

    if y_scale not in ("linear", "log"):
        raise ValueError("y_scale must be 'linear' or 'log'")

    # If log scale, drop non-positive y-values (matplotlib can't plot them)
    if y_scale == "log":
        n_before = len(df)
        df = df[df[y_col] > 0]
        dropped = n_before - len(df)
        if dropped > 0:
            print(
                f"[warn] Dropped {dropped} non-positive {y_col} values for log scale."
            )

    # Build equal-width bins on x
    x_min, x_max = df[x_col].min(), df[x_col].max()
    # Protect against degenerate case
    if x_min == x_max:
        raise ValueError("All x values are identical; cannot create bins.")
    edges = np.linspace(x_min, x_max, num_bins + 1)
    df["__bin"] = pd.cut(df[x_col], bins=edges, include_lowest=True, right=False)

    # Group y by bin, drop empty bins
    grouped = df.groupby("__bin")[y_col].apply(list)
    nonempty = [(interval, vals) for interval, vals in grouped.items() if len(vals) > 0]
    if len(nonempty) == 0:
        raise ValueError("All bins are empty; check your data or num_bins.")

    intervals, data = zip(*nonempty)

    # Prepare labels like "[a, b)" with tidy decimals
    bin_width = (x_max - x_min) / num_bins
    nd = _decimals(bin_width)
    labels = [f"[{iv.left:.{nd}f}, {iv.right:.{nd}f})" for iv in intervals]

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bp = ax.boxplot(
        data,
        positions=np.arange(len(data)),
        widths=0.7,
        showfliers=showfliers,
        patch_artist=True,  # allows filled boxes (uses default colors)
        manage_ticks=False,
    )

    # Light styling (keeps default colors)
    for box in bp["boxes"]:
        box.set_alpha(0.6)
        box.set_linewidth(1.2)
    for whisker in bp["whiskers"]:
        whisker.set_linewidth(1.2)
    for cap in bp["caps"]:
        cap.set_linewidth(1.2)
    for median in bp["medians"]:
        median.set_linewidth(1.4)

    # X axis
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_xlabel(xlabel)

    # Y axis
    ax.set_ylabel(ylabel)
    ax.set_yscale(y_scale)

    # Title & grid
    ax.set_title(title)
    ax.grid(True, axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(save_path)
    print(f"Saved boxplot to {save_path}")
    plt.close(fig)


# --- NEW ALTERNATIVE VERSION: use x values as classes instead of bins ---


def plot_boxplots_from_csv_classes(
    csv_file: str,
    x_col: str,
    y_col: str,
    title: str,
    xlabel: str,
    ylabel: str,
    *,
    classes: Optional[Sequence[Union[str, Number]]] = None,
    drop_unlisted: bool = False,
    sort_classes: bool = True,
    y_scale: str = "linear",
    save_path: str = "boxplot_classes.pdf",
    showfliers: bool = True,
):
    """
    Create boxplots of y-values using the *distinct values of x* as category labels
    ("classes") instead of binning into equal-width intervals.

    This is useful when x already encodes discrete groups (e.g., grades A/B/C,
    models, or discrete numeric settings) or when you want to limit and order the
    shown categories explicitly.

    Parameters
    ----------
    csv_file : str
        Path to the CSV file.
    x_col : str
        Column name for x-values (treated as categorical).
    y_col : str
        Column name for y-values.
    title, xlabel, ylabel : str
        Plot text.
    classes : Sequence[str|number], optional
        If provided, only these x values will be shown *in the given order*.
        If not provided, all unique x values present in the data are used.
    drop_unlisted : bool
        If True, rows whose x value is not in `classes` are dropped. If False,
        unlisted values (if any) will form an extra class at the end when
        `classes` is provided. Ignored if `classes` is None.
    sort_classes : bool
        When `classes` is None, sort the discovered unique x values before plotting.
        For mixed types, values are treated as strings for sorting.
    y_scale : {"linear","log"}
        Y-axis scale. If "log", non-positive y values are dropped (with a warning).
    save_path : str
        Where to save the figure.
    showfliers : bool
        Show outliers in the boxplot.

    Notes
    -----
    - This function is an alternative to `plot_boxplots_from_csv` (binning version).
    - Use it when you want bars = number of *classes* (not number of equal-width bins).
    """

    # Load and clean
    df = pd.read_csv(csv_file)
    df = df.dropna(subset=[x_col, y_col])

    if y_scale not in ("linear", "log"):
        raise ValueError("y_scale must be 'linear' or 'log'")

    if y_scale == "log":
        n_before = len(df)
        df = df[df[y_col] > 0]
        dropped = n_before - len(df)
        if dropped > 0:
            print(
                f"[warn] Dropped {dropped} non-positive {y_col} values for log scale."
            )

    # Determine class labels and order
    if classes is None:
        # Use all unique values present
        uniq = df[x_col].dropna().unique().tolist()
        if sort_classes:
            try:
                uniq = sorted(uniq)
            except Exception:
                # Fallback to string sort for mixed types
                uniq = sorted(uniq, key=lambda v: str(v))
        class_labels = uniq
        # All rows are allowed
        df_filtered = df.copy()
    else:
        class_labels = list(classes)
        if drop_unlisted:
            df_filtered = df[df[x_col].isin(class_labels)].copy()
        else:
            # Keep everything; values not listed go to an "Other" bucket at the end
            df_filtered = df.copy()
            other_mask = ~df_filtered[x_col].isin(class_labels)
            if other_mask.any():
                df_filtered.loc[other_mask, x_col] = "Other"
                if "Other" not in class_labels:
                    class_labels = class_labels + ["Other"]

    if len(class_labels) == 0:
        raise ValueError(
            "No classes to plot. Provide non-empty `classes` or data must contain unique x values."
        )

    # Build data lists in the target order, skipping empty classes
    data: list[list[Number]] = []
    labels: list[str] = []
    for lab in class_labels:
        vals = df_filtered.loc[df_filtered[x_col] == lab, y_col].tolist()
        if len(vals) > 0:
            data.append(vals)
            labels.append(str(lab))

    if len(data) == 0:
        raise ValueError("All classes are empty; check your `classes` list or filters.")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bp = ax.boxplot(
        data,
        positions=np.arange(len(data)),
        widths=0.7,
        showfliers=showfliers,
        patch_artist=True,
        manage_ticks=False,
    )

    # Light styling
    for box in bp["boxes"]:
        box.set_alpha(0.6)
        box.set_linewidth(1.2)
    for whisker in bp["whiskers"]:
        whisker.set_linewidth(1.2)
    for cap in bp["caps"]:
        cap.set_linewidth(1.2)
    for median in bp["medians"]:
        median.set_linewidth(1.4)

    # X axis: one tick per class label
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_xlabel(xlabel)

    # Y axis
    ax.set_ylabel(ylabel)
    ax.set_yscale(y_scale)

    # Title & grid
    ax.set_title(title)
    ax.grid(True, axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(save_path)
    print(f"Saved class-based boxplot to {save_path}")
    plt.close(fig)
