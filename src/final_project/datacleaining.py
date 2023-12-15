import pandas as pd

# Define the file path
file_path = r'C:\Users\admin\Desktop\MEMT680\final_project\src\final_project\FantasyFootballWeekly.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Replace "--" with NaN and drop columns with all NaN values
df.replace("--", pd.NA, inplace=True)
df.dropna(axis=1, how='all', inplace=True)

# Save the cleaned DataFrame back to a CSV file if needed
cleaned_file_path = r'C:\Users\admin\Desktop\MEMT680\final_project\src\final_project\CleanedFantasyFootballWeekly.csv'
df.to_csv(cleaned_file_path, index=False)
