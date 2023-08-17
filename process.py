import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
def processH():
    # Read data from file
    df = pd.read_csv("D:\VIT\Sem_6\IOT -CSE3009\Project/WeatherPrediction/feed.csv",header=None, names=["datetime", "id", "temperature","humidity"])
    
    # Convert datetime string to datetime object
    df["datetime"] = pd.to_datetime(df["datetime"])
    
    # Sort data by datetime
    df = df.sort_values(by="datetime")
    
    # Create new features for hour of day and day of wee
    df["hour"] = df["datetime"].dt.hour
    df["day_of_week"] = df["datetime"].dt.dayofweek
    
    # Create X and y for linear regression
    X = df[["hour", "day_of_week"]]
    y = df["humidity"]
    
    # Fit linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict humidity for next 1 week
    last_datetime = df["datetime"].max()
    next_week_dates = [last_datetime + timedelta(hours=i) for i in range(168)]
    next_week_hours = [date.hour for date in next_week_dates]
    next_week_days_of_week = [date.dayofweek for date in next_week_dates]
    next_week_X = pd.DataFrame(
        {"hour": next_week_hours, "day_of_week": next_week_days_of_week})
    next_week_y = model.predict(next_week_X)
    
    # Print predicted humidity values
    wed = [[] for _ in range(3)]
    for date, humidity in zip(next_week_dates, next_week_y):
        wed.append(
            [formatDate(date.strftime('%Y-%m-%d %H:%M:%S %Z')), humidity])
        return wed
    def processT():
        
        # Read data from file
        df = pd.read_csv("D:\VIT\Sem_6\IOT -CSE3009\Project/WeatherPrediction/feed.csv",header=None, names=["datetime", "id", "temperature", "humidity"])
        
        # Convert datetime string to datetime object
        df["datetime"] = pd.to_datetime(df["datetime"])
        
        # Sort data by datetime
        df = df.sort_values(by="datetime")
        
        # Create new features for hour of day and day of week
        df["hour"] = df["datetime"].dt.hour
        df["day_of_week"] = df["datetime"].dt.dayofweek
        
        # Create X and y for linear regression
        X = df[["hour", "day_of_week"]]
        y = df["temperature"]
        
        # Fit linear regression model
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict temperature for next 1 week
        last_datetime = df["datetime"].max()
        next_week_dates = [last_datetime + timedelta(hours=i) for i in range(168)]
        next_week_hours = [date.hour for date in next_week_dates]
        next_week_days_of_week = [date.dayofweek for date in next_week_dates]
        next_week_X = pd.DataFrame({"hour": next_week_hours, "day_of_week": next_week_days_of_week})
        next_week_y = model.predict(next_week_X)
        
        # Print predicted temperature values
        wed = [[] for _ in range(3)]
        for date, temperature in zip(next_week_dates, next_week_y):
            wed.append([formatDate(date.strftime('%Y-%m-%d %H:%M:%S %Z')), temperature])
            return wed
        def formatDate(date_string):
            date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S %Z')
            formatted_date = date_obj.strftime('%A, %d %B %Y at %I:%M %p %Z')
            return formatted_date