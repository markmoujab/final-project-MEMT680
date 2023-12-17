import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt


df = pd.read_csv('FantasyFootballWeekly_cleaned')

# Filter the dataset to include only QB players
df_qb = df[df['PLAYER POSITION'] == 'QB']

# Select touchdown-related columns as features
touchdowns_features = df_qb[['PASSING TD', 'RUSHING TD', 'RECEIVING TD', 'MISC TD']]

# Target variable
target = df_qb['PROJ']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(touchdowns_features, target, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate R2 score
r2 = r2_score(y_test, predictions)
print(f'R2 Score: {r2}')

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error (MSE): {mse}')

# Plotting predictions vs actual values
plt.scatter(y_test, predictions)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values for Fantasy Football Projections (QB Players)')
plt.show()
