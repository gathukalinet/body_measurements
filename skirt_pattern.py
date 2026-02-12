# skirt_pattern.py
import matplotlib
matplotlib.use("Agg")  # REQUIRED for cloud

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np


def draw_circle_skirt_pattern(waist, length):
    fig, ax = plt.subplots(figsize=(8, 8))

    radius = waist / (2 * np.pi)
    circle = plt.Circle((0, 0), radius, fill=False)
    outer = plt.Circle((0, 0), radius + length, fill=False)

    ax.add_patch(circle)
    ax.add_patch(outer)

    ax.set_aspect("equal")
    ax.axis("off")

    return fig


def export_pattern_pdf(fig, filename="skirt_pattern.pdf"):
    with PdfPages(filename) as pdf:
        pdf.savefig(fig)
    plt.close(fig)
