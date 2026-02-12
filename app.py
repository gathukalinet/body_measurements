import matplotlib
matplotlib.use("Agg")

import streamlit as st
import matplotlib.pyplot as plt

st.title("Matplotlib Test")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

st.pyplot(fig)
