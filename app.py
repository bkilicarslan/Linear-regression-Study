import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Page Configuration (Must be the first Streamlit command)
# 'wide' layout gives us plenty of room for side-by-side columns
st.set_page_config(page_title="Linear Regression App", layout="wide")

# App Header
st.title("Linear Regression Visualizer")
st.write("Edit the data table on the left to instantly update the graph and statistics on the right.")
st.divider() # Adds a nice horizontal line for visual separation

# 2. Create the Layout Columns
# The [1, 2.5] ratio means the right column is 2.5 times wider than the left
col1, col2 = st.columns([1, 2.5])

# --- LEFT COLUMN: DATA INPUT ---
with col1:
    st.subheader("Data Input")
    
    default_data = pd.DataFrame({
        'X': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
        'Y': [2.1, 3.8, 5.2, 4.5, 6.1, 7.3, 8.0, 9.4, 8.9, 11.5]
    })

    # Display the interactive editor
    edited_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)
    
    # Extract data for the math
    x = edited_df['X'].values
    y = edited_df['Y'].values

# --- RIGHT COLUMN: STATS & GRAPH ---
with col2:
    st.subheader("Visualization & Statistics")
    
    if len(x) > 1:
        # Calculate regression and correlation
        slope, intercept = np.polyfit(x, y, 1)
        correlation_matrix = np.corrcoef(x, y)
        correlation_coefficient = correlation_matrix[0, 1]
        line_equation = f"y = {slope:.2f}x + {intercept:.2f}"

        # Dashboard-style metrics for the stats
        stat_col1, stat_col2 = st.columns(2)
        stat_col1.metric(label="Linear Equation", value=line_equation)
        stat_col2.metric(label="Correlation (r)", value=f"{correlation_coefficient:.4f}")

        # Generate the plot
        # Increased figsize slightly to fit the wider column perfectly
        fig, ax = plt.subplots(figsize=(8, 5)) 
        ax.scatter(x, y, color='blue', label='Data Points', zorder=2)
        
        regression_line = slope * x + intercept
        ax.plot(x, regression_line, color='red', label=f'Fit: {line_equation}', zorder=1)

        ax.set_title("Scatter Plot with Linear Regression")
        ax.set_xlabel("X-Axis Variable")
        ax.set_ylabel("Y-Axis Variable")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        # Render the plot
        st.pyplot(fig)
    else:
        st.warning("Please enter at least two data points to calculate the regression.")
