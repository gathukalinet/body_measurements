import streamlit as st
import tempfile
# Ensure these functions exist in your skirt_pattern.py file
from skirt_pattern import draw_circle_skirt_pattern, export_pattern_pdf

st.set_page_config(
    page_title="Circle Skirt Pattern Generator",
    layout="centered",
)

st.title("🪡 Circle Skirt Pattern Generator")

with st.form("measurements_form"):
    skirt_type = st.selectbox(
        "Skirt type",
        ["full", "half", "quarter"],
        format_func=lambda x: x.capitalize() + " Circle",
        key="skirt_type_v2"
    )

    # We use 'value=' to set a safe default, and 'key=' to bypass the browser's memory
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, key="w_v2")
    height = st.number_input("Height (cm)", min_value=120.0, max_value=220.0, value=165.0, key="h_v2")
    waist = st.number_input("Waist circumference (cm)", min_value=50.0, max_value=150.0, value=75.0, key="waist_v2")
    hip = st.number_input("Hip circumference (cm)", min_value=60.0, max_value=180.0, value=95.0, key="hip_v2")
    skirt_length = st.number_input("Preferred skirt length (cm)", min_value=30.0, max_value=120.0, value=50.0, key="len_v2")

    submitted = st.form_submit_button("Generate Pattern ✂️")

if submitted:
    st.info("Creating your pattern...")
    fig = draw_circle_skirt_pattern(
        waist_cm=waist,
        hip_cm=hip,
        height_cm=height,
        weight_kg=weight,
        skirt_length_cm=skirt_length,
        circle_type=skirt_type,
    )

    st.pyplot(fig)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        export_pattern_pdf(fig, tmp.name)
        with open(tmp.name, "rb") as pdf_file:
            st.download_button(
                label="📄 Download PDF Pattern",
                data=pdf_file,
                file_name=f"{skirt_type}_skirt.pdf",
                mime="application/pdf",
            )