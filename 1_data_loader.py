import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print("File not found!")
        return None

if __name__ == "__main__":
    df = load_data("data.csv")
    print(df.head())
