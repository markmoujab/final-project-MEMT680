# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset
file_path = r'C:\Users\admin\Desktop\MEMT680\final_project\src\final_project\FantasyFootballWeekly.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, low_memory=False)
df = df.infer_objects()

# Drop rows where the target column has '--' as the value
df = df[df['TOTAL'] != '--']

# Convert the 'TOTAL' column to numeric
df['TOTAL'] = pd.to_numeric(df['TOTAL'], errors='coerce')

# Separate features (X) and target variable (y)
X = df.drop('TOTAL', axis=1)
y = df['TOTAL']

# Identify categorical columns
categorical_columns = X.select_dtypes(include=['object']).columns

# Create transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), X.columns.difference(categorical_columns)),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
    ])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit and transform the data using the preprocessor
X_train_scaled = preprocessor.fit_transform(X_train)
X_test_scaled = preprocessor.transform(X_test)

# Initialize the Dummy Regressor model
model = DummyRegressor(strategy="mean")  # You can also use "median" or "constant" as the strategy

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the number of rows after processing for the test data
print(f"Number of rows after processing (test): {X_test_scaled.shape[0]}")
print(f"Number of rows after processing (train): {X_train_scaled.shape[0]}")

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
