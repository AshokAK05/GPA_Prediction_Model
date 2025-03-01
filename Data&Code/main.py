import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, request, render_template
import joblib
import os

# Load dataset
file_path = "cleaned_student.csv"  # Ensure the cleaned dataset is in the same directory
df = pd.read_csv(file_path)

# Select relevant features for predicting GPA
features = ['StudyTimeWeekly', 'Absences', 'ParentalSupport', 'Tutoring', 'Extracurricular']
target = 'GPA'

# Drop rows with missing values
df = df.dropna(subset=features + [target])

# Define features (X) and target variable (y)
X = df[features]
y = df[target]

# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train, y_train)

# Save the model
joblib.dump(rf_reg, 'gpa_model.pkl')
joblib.dump(features, 'features.pkl')

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        try:
            model = joblib.load('gpa_model.pkl')
            features = joblib.load('features.pkl')

            # Get user input safely
            input_data = [float(request.form.get(f, 0)) for f in features]

            # Convert input to DataFrame
            input_df = pd.DataFrame([input_data], columns=features)

            # Make prediction
            prediction = round(model.predict(input_df)[0], 2)  # Round to 2 decimal places
        except Exception as e:
            prediction = f"Error: {str(e)}"  # Handle any errors

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
