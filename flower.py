import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 1000)
r = 1 + np.sin(6 * theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([])

st.pyplot(fig)
