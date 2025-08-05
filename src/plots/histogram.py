from src.setup import thesis_figure
import pandas as pd
import matplotlib.pyplot as plt


def plot_histogram(
    csv_file,
    column,
    bins,
    title,
    xlabel,
    ylabel,
    xticks,
    xticklabels,
    save_path="plot.pdf",
    text_color="red",
    fontsize_ticks=12,
    fontsize_text=10,
    ylim_factor=1.1,
    edgecolor="black",
):
    """
    Plot a histogram for a specified column in a CSV file with customizable parameters.

    Parameters:
    ----------
    csv_file : str
        Path to the CSV file containing the data.
    column : str
        Column name in the CSV to plot.
    bins : list or int
        Bin edges or number of bins for the histogram.
    title : str
        Title of the histogram plot.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.
    xticks : list
        Positions of the x-axis ticks.
    xticklabels : list
        Labels corresponding to `xticks`.
    save_path : str, optional
        Path to save the figure. Default is "plot.pdf".
    text_color : str, optional
        Color of the text annotations. Default is "red".
    fontsize_ticks : int, optional
        Font size for x-tick labels. Default is 12.
    fontsize_text : int, optional
        Font size for count labels above bars. Default is 10.
    ylim_factor : float, optional
        Multiplier for setting y-axis upper limit. Default is 1.1.
    edgecolor : str, optional
        Color for the edges of histogram bars. Default is "black".
    """

    df = pd.read_csv(csv_file)

    fig, ax = plt.subplots()
    counts, bins_out, patches = ax.hist(df[column], bins=bins, edgecolor=edgecolor)

    # Set axis labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Set x-ticks and labels
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, fontsize=fontsize_ticks)

    # Annotate counts on top of bars
    for count, patch in zip(counts, patches):
        x = patch.get_x() + patch.get_width() / 2
        y = patch.get_height()
        ax.text(
            x,
            y + 0.1,
            int(count),
            ha="center",
            va="bottom",
            color=text_color,
            fontsize=fontsize_text,
        )

    # Set y-axis limit
    ax.set_ylim(top=max(counts) * ylim_factor)

    # Adjust layout and save
    fig.tight_layout()
    fig.savefig(save_path)
    plt.close(fig)
