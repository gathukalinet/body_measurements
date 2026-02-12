# app.py
import streamlit as st
from skirt_pattern import draw_circle_skirt_pattern, export_pattern_pdf

st.title("Circle Skirt Pattern Generator")

waist = st.number_input("Waist (cm)", 50.0, 150.0)
length = st.number_input("Length (cm)", 30.0, 120.0)

if st.button("Generate pattern"):
    fig = draw_circle_skirt_pattern(waist, length)
    st.pyplot(fig)

    export_pattern_pdf(fig)
    with open("skirt_pattern.pdf", "rb") as f:
        st.download_button(
            "Download PDF",
            f,
            file_name="skirt_pattern.pdf",
            mime="application/pdf",
        )
