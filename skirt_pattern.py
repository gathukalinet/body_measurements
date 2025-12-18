
import numpy as np
import matplotlib.pyplot as plt


def circle_skirt_radii(waist_cm, skirt_length_cm, circle_type="full"):
    """
    Compute inner and outer radius based on skirt type.
    """
    divisor = {
        "full": 2 * np.pi,
        "half": np.pi,
        "quarter": np.pi / 2,
    }

    if circle_type not in divisor:
        raise ValueError("circle_type must be 'full', 'half', or 'quarter'")

    inner_radius = waist_cm / divisor[circle_type]
    outer_radius = inner_radius + skirt_length_cm

    return inner_radius, outer_radius


def draw_arc(ax, radius, theta_max, **kwargs):
    theta = np.linspace(0, theta_max, 400)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y, **kwargs)


def draw_circle_skirt_pattern(
    waist_cm,
    hip_cm,
    height_cm,
    weight_kg,
    skirt_length_cm,
    circle_type="full",
    seam_allowance_cm=1.5,
):
    inner_r, outer_r = circle_skirt_radii(
        waist_cm, skirt_length_cm, circle_type
    )

    fig, ax = plt.subplots(figsize=(8, 8))

    theta_max = {
        "full": 2 * np.pi,
        "half": np.pi,
        "quarter": np.pi / 2,
    }[circle_type]

    # Waist curve
    draw_arc(ax, inner_r, theta_max, linestyle="--", linewidth=2, label="Waist")

    # Hem curve
    draw_arc(ax, outer_r, theta_max, linewidth=2, label="Hem")

    # Seam allowance
    draw_arc(
        ax,
        outer_r + seam_allowance_cm,
        theta_max,
        linestyle=":",
        linewidth=1.5,
        label="Hem Seam Allowance",
    )

    # Side seams (straight lines)
    ax.plot([0, outer_r], [0, 0], linewidth=1)
    if circle_type != "full":
        ax.plot(
            [0, outer_r * np.cos(theta_max)],
            [0, outer_r * np.sin(theta_max)],
            linewidth=1,
        )

    ax.set_aspect("equal")
    ax.axis("off")

    padding = outer_r + 5
    ax.set_xlim(-5, padding)
    ax.set_ylim(-5, padding)

    ax.legend(loc="upper right")

    ax.set_title(
        f"{circle_type.capitalize()} Circle Skirt Pattern\n"
        f"Waist: {waist_cm} cm | Length: {skirt_length_cm} cm",
        fontsize=12,
    )

    return fig


def export_pattern_pdf(fig, filename="circle_skirt_pattern.pdf"):
    fig.savefig(filename, format="pdf", bbox_inches="tight")

