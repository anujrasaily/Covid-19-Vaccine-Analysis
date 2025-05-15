import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from 2_data_cleaner import clean_data
from 1_data_loader import load_data

def plot_vaccine_usage(df):
    sns.barplot(x="Country", y="Doses_Administered", data=df)
    plt.title("Total Doses Administered per Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_vaccination_rate(df):
    sns.barplot(x="Country", y="Vaccination_Rate", data=df)
    plt.title("Vaccination Rate per Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = clean_data(load_data("data.csv"))
    plot_vaccine_usage(df)
    plot_vaccination_rate(df)
