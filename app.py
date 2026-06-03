import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. App Header and Description
st.title("Linear Regression Visualizer")
st.write("Edit the data table below to instantly update the scatter plot and regression line.")

# 2. Set up the interactive data table
# We provide some default data to start with
default_data = pd.DataFrame({
    'X': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
    'Y': [2.1, 3.8, 5.2, 4.5, 6.1, 7.3, 8.0, 9.4, 8.9, 11.5]
})

# st.data_editor allows the user to add, delete, or change numbers on the web page
edited_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

# Extract the updated columns into NumPy arrays
x = edited_df['X'].values
y = edited_df['Y'].values

# 3. Math & Plotting Logic (Only runs if there are at least 2 points)
if len(x) > 1:
    # Calculate regression
    slope, intercept = np.polyfit(x, y, 1)
    correlation_matrix = np.corrcoef(x, y)
    correlation_coefficient = correlation_matrix[0, 1]
    
    line_equation = f"y = {slope:.2f}x + {intercept:.2f}"

    # Display results on the app
    st.subheader("Statistical Results")
    st.write(f"**Linear Regression Equation:** ${line_equation}$")
    st.write(f"**Correlation Coefficient (r):** {correlation_coefficient:.4f}")

    # Generate the plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Data Points', zorder=2)
    
    regression_line = slope * x + intercept
    ax.plot(x, regression_line, color='red', label=f'Fit: {line_equation}', zorder=1)

    ax.set_title("Scatter Plot with Linear Regression")
    ax.set_xlabel("X-Axis Variable")
    ax.set_ylabel("Y-Axis Variable")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    # Render the plot in Streamlit
    st.pyplot(fig)
else:
    st.warning("Please enter at least two data points to calculate the regression.")
