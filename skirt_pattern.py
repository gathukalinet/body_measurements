import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def draw_circle_skirt_pattern(waist_cm, hip_cm, height_cm, weight_kg, skirt_length_cm, circle_type):
    # 1. Calculate Radii
    if circle_type == "full":
        angle = np.pi / 2  
        r_waist = waist_cm / (2 * np.pi)
    elif circle_type == "half":
        angle = np.pi / 2 
        r_waist = waist_cm / np.pi
    else:  # quarter
        angle = np.pi / 2
        r_waist = waist_cm / (np.pi / 2)

    r_hem = r_waist + skirt_length_cm
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 2. Draw the Arcs
    t = np.linspace(0, angle, 100)
    ax.plot(r_waist * np.cos(t), r_waist * np.sin(t), 'black', lw=3) 
    ax.plot(r_hem * np.cos(t), r_hem * np.sin(t), 'black', lw=4)     
    
    # 3. Draw Straight Edges
    ax.plot([r_waist, r_hem], [0, 0], 'black', lw=3)
    ax.plot([0, 0], [r_waist, r_hem], 'black', lw=3)

    # 4. Add the Grainline (Bias Grain)
    # Positioning the arrow at the 45-degree mark (pi/4)
    grain_angle = np.pi / 4
    # Arrow length is about 40% of the skirt length
    arrow_len = skirt_length_cm * 0.4
    center_r = r_waist + (skirt_length_cm / 2)
    
    # Calculate start and end points for a double-headed arrow
    x_start = (center_r - arrow_len/2) * np.cos(grain_angle)
    y_start = (center_r - arrow_len/2) * np.sin(grain_angle)
    x_end = (center_r + arrow_len/2) * np.cos(grain_angle)
    y_end = (center_r + arrow_len/2) * np.sin(grain_angle)

    ax.annotate('', xy=(x_end, y_end), xytext=(x_start, y_start),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax.text(x_start, y_start - 2, "GRAINLINE (BIAS)", color='blue', 
            rotation=45, fontweight='bold', fontsize=9)

    # 5. Set explicit limits
    limit = r_hem * 1.1
    ax.set_xlim(-8, limit)
    ax.set_ylim(-8, limit)

    # 6. Labels
    label_style = {'fontweight': 'bold', 'fontsize': 10}
    mid_point = r_waist + (skirt_length_cm / 2)
    
    if circle_type == "full":
        ax.text(mid_point, -4, "PLACE ON FOLD", ha='center', **label_style)
        ax.text(-4, mid_point, "PLACE ON FOLD", rotation=90, va='center', **label_style)
        title_extra = "(Cut 1 on double fold)"
    elif circle_type == "half":
        ax.text(mid_point, -4, "PLACE ON FOLD", ha='center', **label_style)
        ax.text(-4, mid_point, "SEAM LINE", rotation=90, va='center', color='red', **label_style)
        title_extra = "(Cut 1 on fold)"
    else:
        ax.text(mid_point, -4, "SEAM LINE", ha='center', color='red', **label_style)
        ax.text(-4, mid_point, "SEAM LINE", rotation=90, va='center', color='red', **label_style)
        title_extra = "(Cut 2 mirrored)"

    ax.set_aspect('equal')
    ax.axis('off')
    plt.title(f"{circle_type.capitalize()} Circle Skirt Layout {title_extra}", pad=20)
    
    return fig

def export_pattern_pdf(fig, filename):
    with PdfPages(filename) as pdf:
        pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)
