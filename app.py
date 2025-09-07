import streamlit as st
import pandas as pd
import altair as alt
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv('forecasting_dataset.csv', parse_dates=['Date'])

# Train regression model
X = df[['Irradiance (kWh/m²)', 'Temperature (°C)', 'Humidity (%)']]
y = df['Solar Output (MWh)']
model = LinearRegression().fit(X, y)
df['Predicted Output'] = model.predict(X)

# Define scatter plot function
def make_scatter_chart(data, x_variable):
    chart = alt.Chart(data).mark_circle(size=60).encode(
        x=alt.X(x_variable, title=x_variable),
        y=alt.Y('Solar Output (MWh)', title='Solar Output (MWh)'),
        tooltip=[x_variable, 'Solar Output (MWh)', 'Date']
    ).properties(
        title=f'Solar Output vs {x_variable}'
    ).interactive()
    return chart

# Sidebar controls
st.sidebar.header("Filters & Inputs")

# Date range filter
min_date, max_date = df['Date'].min(), df['Date'].max()
date_range = st.sidebar.date_input(
    "Select date range",
    [min_date.date(), max_date.date()]
)

# Filter dataframe based on selected dates
if len(date_range) == 2:
    start_date, end_date = date_range
    start_date = pd.Timestamp(start_date)  # Convert to Timestamp for comparison
    end_date = pd.Timestamp(end_date)
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df_filtered = df.loc[mask]
else:
    df_filtered = df.copy()

# Dropdown to select scatter plot variable
x_var = st.sidebar.selectbox(
    "Select variable for scatter plot X-axis",
    ["Irradiance (kWh/m²)", "Temperature (°C)", "Humidity (%)"]
)

# Sliders for what-if analysis
st.sidebar.subheader("Adjust inputs for prediction:")
irr_val = st.sidebar.slider("Irradiance (kWh/m²)", 0.0, 10.0, 5.0, step=0.1)
temp_val = st.sidebar.slider("Temperature (°C)", 0.0, 40.0, 25.0, step=0.5)
hum_val = st.sidebar.slider("Humidity (%)", 0, 100, 50, step=1)
pred_val = model.predict([[irr_val, temp_val, hum_val]])[0]

# Main dashboard
st.title("Solar Output Regression Dashboard")
r2_score = model.score(X, y)
st.write(f"Data from {min_date.date()} to {max_date.date()}. Model R² = {r2_score:.2f}")

# Line chart: Actual vs Predicted over time (filtered)
st.subheader("Actual vs Predicted Output over Time")
st.line_chart(df_filtered.set_index('Date')[['Solar Output (MWh)', 'Predicted Output']])

# Scatter plot
st.subheader(f"Solar Output vs {x_var}")
st.altair_chart(make_scatter_chart(df_filtered, x_var), use_container_width=True)

# What-if prediction result
st.subheader("What-if Prediction")
st.write(f"For Irradiance={irr_val}, Temperature={temp_val}, Humidity={hum_val}: "
         f"**Predicted Output = {pred_val:.3f} MWh**")