import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Straight Line Plotter")

# User inputs for slope and intercept
m = st.number_input("Enter the slope (m):", value=1.0)
c = st.number_input("Enter the y-intercept (c):", value=0.0)

# Generate x and y values
x = np.linspace(-10, 10, 100)
y = m * x + c

# Plot the line
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {m}x + {c}")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True)
ax.legend()

# Display plot in Streamlit
st.pyplot(fig)
