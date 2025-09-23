# pizza_game_streamlit.py

import streamlit as st
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="🍕 Pizza Game", layout="centered")

# Initialize session state
if "total_slices" not in st.session_state:
    st.session_state.total_slices = 8
    st.session_state.remaining_slices = list(range(8))  # slice indices still uneaten

# Function to "eat" a slice
def eat_slice(slice_index):
    if slice_index in st.session_state.remaining_slices:
        st.session_state.remaining_slices.remove(slice_index)

# Display pizza
fig, ax = plt.subplots()
ax.set_aspect("equal")

# Colors for slices
colors = ["#FF5733", "#FFC300", "#DAF7A6", "#FF33A8",
          "#33FFF3", "#A633FF", "#FF8C33", "#33FF57"]

# Draw each slice, color if uneaten, white if eaten
slice_colors = [
    colors[i % len(colors)] if i in st.session_state.remaining_slices else "white"
    for i in range(st.session_state.total_slices)
]

wedges, _ = ax.pie([1]*st.session_state.total_slices, colors=slice_colors, startangle=90)
ax.set_title(" Click a slice button to eat it!")

st.pyplot(fig)

# Buttons for each slice
cols = st.columns(st.session_state.total_slices)
for i, col in enumerate(cols):
    if i in st.session_state.remaining_slices:
        # Add a unique key for each button
        if col.button(f"Eat Slice {i+1}", key=f"slice_{i}"):
            eat_slice(i)

# Show remaining fraction
remaining = len(st.session_state.remaining_slices)
if remaining > 0:
    st.subheader(f"{remaining}/{st.session_state.total_slices} slices left")
else:
    st.subheader("No pizza left! 😭")

