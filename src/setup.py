# Configure matplotlib
import matplotlib
import matplotlib.pyplot as plt
import scienceplots


def thesis_figure(figsize=(6.0, 4.0)):
    plt.style.use(["science", "nature"])
    plt.rcParams.update(
        {
            "pgf.texsystem": "pdflatex",
            "pgf.rcfonts": False,
            "pgf.preamble": "\n".join(
                [
                    r"\usepackage[utf8]{inputenc}",
                    r"\usepackage[T1]{fontenc}",
                    r"\usepackage[ngerman]{babel}",
                    r"\usepackage{lmodern}",
                    r"\usepackage{amsmath}",
                    r"\usepackage{siunitx}",
                    r"\sisetup{locale=DE}",
                    r"\usepackage{xcolor}",
                    r"\providecommand{\mathdefault}[1]{#1}",
                    r"\DeclareSIUnit{\torr}{Torr}",
                ]
            ),
            "font.family": "serif",
            "font.size": 12,
            "xtick.labelsize": 12,  # x tick labels
            "ytick.labelsize": 12,  # y tick labels
            "axes.labelsize": 12,  # x/y axis labels
            "axes.titlesize": 13,  # title font size
            "legend.fontsize": 11,
            "figure.dpi": 300,
            "text.usetex": True,  # match LaTeX font (optional)
        }
    )

    return plt.subplots(figsize=figsize, dpi=300)
