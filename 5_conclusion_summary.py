from 4_vaccine_efficiency import calculate_efficiency
from 1_data_loader import load_data
from 2_data_cleaner import clean_data

def generate_summary(df):
    highest = df.loc[df['Vaccination_Rate'].idxmax()]
    print(f"✅ Country with highest vaccination rate: {highest['Country']} using {highest['Vaccine']}")

if __name__ == "__main__":
    df = clean_data(load_data("data.csv"))
    generate_summary(df)
