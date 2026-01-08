"""
Netflix Revenue Forecasting & Time Series Analysis
===================================================
Author: Vinisha Biju
Project: Netflix Business Analytics  
Description: ARIMA-based revenue forecasting with seasonal decomposition
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
import os

warnings.filterwarnings('ignore')

class NetflixRevenueForecaster:
    def __init__(self):
        self.revenue_data = None
        self.model = None
        self.output_dir = 'outputs/results'
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_revenue_data(self):
        quarters = pd.date_range(start='2020-01', end='2024-12', freq='Q')
        base_revenue = [6.15, 6.44, 6.77, 7.16, 7.49, 7.87, 8.28, 8.71,
                       9.19, 9.67, 10.19, 10.74, 11.31, 11.93, 12.58, 13.25,
                       13.96, 14.72, 15.51, 16.35]
        
        self.revenue_data = pd.DataFrame({
            'quarter': quarters,
            'revenue_billions': base_revenue
        })
        self.revenue_data.set_index('quarter', inplace=True)
        return self
    
    def train_arima_model(self):
        print("Training ARIMA(1,1,1) model...")
        self.model = ARIMA(self.revenue_data['revenue_billions'], order=(1, 1, 1))
        self.model_fit = self.model.fit()
        print("Model trained successfully")
        return self
    
    def generate_forecast(self, periods=12):
        forecast = self.model_fit.forecast(steps=periods)
        last_date = self.revenue_data.index[-1]
        forecast_dates = pd.date_range(start=last_date + pd.DateOffset(months=3), periods=periods, freq='Q')
        
        forecast_df = pd.DataFrame({
            'quarter': forecast_dates,
            'forecasted_revenue_billions': forecast
        })
        forecast_df.set_index('quarter', inplace=True)
        forecast_df.to_csv(f'{self.output_dir}/revenue_forecast.csv')
        print(f"Forecast saved: {self.output_dir}/revenue_forecast.csv")
        return forecast_df
    
    def run_complete_forecast(self):
        print("Netflix Revenue Forecasting Pipeline")
        self.create_revenue_data()
        self.train_arima_model()
        forecast_df = self.generate_forecast(periods=12)
        print("Revenue forecasting completed!")
        return self

if __name__ == "__main__":
    forecaster = NetflixRevenueForecaster()
    forecaster.run_complete_forecast()
