# pizza_game_streamlit.py

import streamlit as st
import matplotlib.pyplot as plt
import random

# Set page title
st.set_page_config(page_title="🍕 Pizza Game", layout="centered")

# Initialize session state
if "total_slices" not in st.session_state:
    st.session_state.total_slices = 8
    st.session_state.remaining_slices = list(range(8))  # slice indices still uneaten

# Function to "eat" a slice by index
def eat_slice(slice_index):
    if slice_index in st.session_state.remaining_slices:
        st.session_state.remaining_slices.remove(slice_index)

# Function to eat one random slice
def eat_one_random():
    if st.session_state.remaining_slices:
        slice_index = random.choice(st.session_state.remaining_slices)
        eat_slice(slice_index)

# Display pizza
fig, ax = plt.subplots()
ax.set_aspect("equal")

# --- Colors for slices (cheese-like shades) ---
colors = ["#FFD700", "#FFA500", "#FFCC66", "#FFB347",
          "#FFDB58", "#FFAE42", "#F4A300", "#FFC04D"]

# Draw each slice, color if uneaten, white if eaten
slice_colors = [
    colors[i % len(colors)] if i in st.session_state.remaining_slices else "white"
    for i in range(st.session_state.total_slices)
]

wedges, _ = ax.pie(
    [1] * st.session_state.total_slices,
    colors=slice_colors,
    startangle=90,
    wedgeprops={"edgecolor": "saddlebrown", "linewidth": 2}  # 🍕 crust effect
)

ax.set_title(" Click below to eat a slice!")

# --- Add toppings (small red dots for pepperoni look) ---
for w in wedges:
    if w.get_facecolor() != (1.0, 1.0, 1.0, 1.0):  # not eaten slice
        x = (w.center[0] + w.r * 0.6 * (w.theta1 + w.theta2) / 360)
        y = (w.center[1] + w.r * 0.6 * (w.theta1 + w.theta2) / 360)
        ax.plot([0], [0], "ro", markersize=6, alpha=0.7)

st.pyplot(fig)

# --- Buttons ---
col1, col2 = st.columns(2)

with col1:
    # One button for each slice
    for i in range(st.session_state.total_slices):
        if i in st.session_state.remaining_slices:
            if st.button(f"Eat Slice {i+1}", key=f"slice_{i}"):
                eat_slice(i)

with col2:
    # New button: Eat one random slice
    if st.button("Eat 1 Slice 🍴"):
        eat_one_random()

# --- Show remaining fraction ---
remaining = len(st.session_state.remaining_slices)
if remaining > 0:
    st.subheader(f"🍕 {remaining}/{st.session_state.total_slices} slices left")
    st.write(f"Fraction left = {remaining}/{st.session_state.total_slices} = {remaining/st.session_state.total_slices:.2f}")
else:
    st.subheader("No pizza left! 😭")

