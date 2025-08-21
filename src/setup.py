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
            "font.size": 14,  # base font size
            "xtick.labelsize": 13,  # tick labels
            "ytick.labelsize": 13,
            "axes.labelsize": 14,  # axis labels
            "axes.titlesize": 16,  # plot titles
            "legend.fontsize": 13,  # legend
            "figure.titlesize": 18,  # suptitle (if you use plt.suptitle)
            "figure.dpi": 300,
            "text.usetex": True,  # match LaTeX font (optional)
        }
    )

    return plt.subplots(figsize=figsize, dpi=300)
