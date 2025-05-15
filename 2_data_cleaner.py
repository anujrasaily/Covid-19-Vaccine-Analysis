import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    df['Vaccination_Rate'] = df['Fully_Vaccinated'] / df['Population']
    df['Dose_Per_Capita'] = df['Doses_Administered'] / df['Population']
    return df

if __name__ == "__main__":
    from 1_data_loader import load_data
    df = load_data("data.csv")
    df = clean_data(df)
    print(df)
