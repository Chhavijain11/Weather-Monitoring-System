# Weather Prediction Web Application

## Overview
This project is a weather prediction web application that uses a linear regression model to forecast temperature and humidity for the upcoming week. It utilizes Flask for the web interface and pandas for data processing.

## Features
- **Process Historical Data**: Reads and processes weather data from a CSV file.
- **Predict Temperature and Humidity**: Uses linear regression to predict weather conditions for the next seven days.
- **Web Interface**: Built with Flask to display predictions.

## Installation
Ensure you have Python installed, then install the dependencies:
```bash
pip install flask pandas scikit-learn
```

## Running the Application
Run the Flask app using the following command:
```bash
python generate.py
```
The application will be accessible at `http://127.0.0.1:5000/`.

## Usage
1. **Home Page** (`/`)
   - Displays the web interface.
2. **Predict Humidity** (`/apih`)
   - Calls the `processH()` function to predict humidity.
3. **Predict Temperature** (`/apit`)
   - Calls the `processT()` function to predict temperature.

## Code Structure
- **`process.py`**: Contains functions for processing weather data and generating predictions.
- **`generate.py`**: Implements the Flask web server and routes.
- **`feed.csv`**: CSV file containing historical weather data.
- **`templates/index.html`**: Web interface template.

## Known Issues
- Ensure the `feed.csv` file exists in the correct directory.
- Predictions are based on a simple linear regression model, which may not capture complex weather pattern.
