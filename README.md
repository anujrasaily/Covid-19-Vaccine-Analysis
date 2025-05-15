# Covid-19 Vaccine Analysis

This project performs data analysis on COVID-19 vaccine distribution and efficiency using Python.

## 📂 Project Structure

covid19_vaccine_analysis/
│
├── data.csv # Dataset containing vaccination records
├── 1_data_loader.py # Script to load the dataset
├── 2_data_cleaner.py # Script to clean and preprocess the data
├── 3_data_visualizer.py # Script to visualize the data
├── 4_vaccine_efficiency.py # Script to analyze vaccine efficiency
├── 5_conclusion_summary.py # Script to print final insights
└── README.md # Project documentation


## 📊 Sample Data Columns

- Country
- Vaccine
- Doses_Administered
- Fully_Vaccinated
- Population
- Date

## 🗃️ Data Structure

The `data.csv` file should have the following columns:

| Column Name         | Description                                      |
|---------------------|--------------------------------------------------|
| Country             | Name of the country                              |
| Vaccine             | Type of vaccine used                             |
| Doses_Administered  | Total doses of vaccine administered              |
| Fully_Vaccinated    | Total number of people fully vaccinated          |
| Population          | Total population of the country                  |
| Date                | Date of data collection (YYYY-MM-DD)             |

## 📦 Requirements

Install the required libraries:

```bash📌 Notes
You can update data.csv with real-world data from trusted sources.

Designed for beginners in data analytics and Python.

🧠 Author
Anuj Rasaily

📧 rasaily239@gmail.com
pip install pandas matplotlib seaborn

🚀 How to Run
Make sure data.csv is in the same folder.

Run each script in order or run them independently as needed.
python 1_data_loader.py
python 2_data_cleaner.py
python 3_data_visualizer.py
python 4_vaccine_efficiency.py
python 5_conclusion_summary.py

