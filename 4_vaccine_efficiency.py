from 2_data_cleaner import clean_data
from 1_data_loader import load_data
import pandas as pd

def calculate_efficiency(df):
    efficiency = df[['Country', 'Vaccine', 'Vaccination_Rate']].sort_values(by='Vaccination_Rate', ascending=False)
    return efficiency

if __name__ == "__main__":
    df = clean_data(load_data("data.csv"))
    result = calculate_efficiency(df)
    print("Efficiency Analysis:\n", result)
