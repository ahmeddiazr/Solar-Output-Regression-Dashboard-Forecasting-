# Solar Output Regression Dashboard

A Streamlit-based interactive dashboard for analyzing and predicting solar power output using machine learning regression models.

## Features

- **Interactive Data Visualization**: View solar output trends over time with actual vs predicted values
- **Scatter Plot Analysis**: Explore relationships between solar output and environmental factors
- **What-if Analysis**: Use interactive sliders to predict solar output under different conditions
- **Date Range Filtering**: Focus analysis on specific time periods
- **Real-time Predictions**: Linear regression model provides instant predictions

## Dashboard Components

### 1. Time Series Analysis
- Line chart showing actual vs predicted solar output over time
- Date range filtering for focused analysis

### 2. Correlation Analysis
- Interactive scatter plots for exploring relationships between:
  - Solar Output vs Irradiance
  - Solar Output vs Temperature  
  - Solar Output vs Humidity

### 3. Predictive Modeling
- Linear regression model trained on environmental factors
- Interactive sliders for what-if scenario analysis
- Real-time prediction updates

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd solar-output-dashboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your dataset (`forecasting_dataset.csv`) is in the project directory with the following columns:
   - `Date`: Date column (will be parsed as datetime)
   - `Irradiance (kWh/m²)`: Solar irradiance measurements
   - `Temperature (°C)`: Temperature readings
   - `Humidity (%)`: Humidity percentage
   - `Solar Output (MWh)`: Target variable for prediction

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the displayed local URL (typically `http://localhost:8501`)

## Data Requirements

The dashboard expects a CSV file named `forecasting_dataset.csv` with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| Date | datetime | Date of measurement |
| Irradiance (kWh/m²) | float | Solar irradiance level |
| Temperature (°C) | float | Ambient temperature |
| Humidity (%) | int/float | Relative humidity percentage |
| Solar Output (MWh) | float | Actual solar power output |

## Model Information

- **Algorithm**: Linear Regression (scikit-learn)
- **Features**: Irradiance, Temperature, Humidity
- **Target**: Solar Output (MWh)
- **Evaluation**: R² score displayed on dashboard

## Dependencies

- streamlit==1.28.1
- pandas==2.0.3
- altair==5.1.2
- scikit-learn==1.3.2
- numpy==1.24.3

## Project Structure

```
solar-output-dashboard/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── forecasting_dataset.csv     # Dataset (not included)
└── README.md                  # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

- [ ] Support for additional regression models (Random Forest, SVR, etc.)
- [ ] Model performance metrics dashboard
- [ ] Data export functionality
- [ ] Advanced filtering options
- [ ] Seasonal analysis features
- [ ] Weather forecast integration
