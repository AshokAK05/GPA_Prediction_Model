# GPA Prediction Model

This project builds a machine learning model to predict a student's **GPA (Grade Point Average)** based on study habits, attendance, and other factors. It includes data preprocessing, model training, and a Flask-based web application.

## Features
✅ Predict GPA based on key factors like **study hours, attendance, and tutoring**  
✅ Uses **Random Forest Regression** for accurate predictions  
✅ **Flask web app** for easy user interaction  
✅ **Preprocessed dataset** to ensure clean and structured data  

---
## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/gpa-prediction.git
cd gpa-prediction
```
### 2. Install Dependencies
```sh
pip install -r requirements.txt
```
If using Pipenv:
```sh
pipenv install
```

### 3. Run Data Preprocessing
```sh
python clean_main.py
```
This script cleans the dataset (`student.csv`) and saves it as `cleaned_student.csv`.

### 4. Train the Model
```sh
python main.py
```
This script:
- Loads the cleaned dataset
- Trains a **Random Forest Regressor**
- Saves the model as `gpa_model.pkl`
- Saves the feature list as `features.pkl`

---
## Running the Web App
```sh
python main.py
```
The Flask app will start, and you can access it at:
```
http://127.0.0.1:5000/
```
Enter study hours, absences, and other details to get a **GPA prediction**.

---
## Project Structure
```
📂 gpa-prediction
│── clean_main.py          # Data cleaning script
│── main.py                # Model training and Flask app
│── student.csv            # Raw dataset
│── cleaned_student.csv     # Preprocessed dataset
│── gpa_model.pkl          # Trained model
│── features.pkl           # Feature list
│── templates/
│   └── index.html         # Web app interface
│── Pipfile                # Pipenv dependencies
│── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

---
## Technologies Used
- **Python** (Pandas, NumPy, Scikit-Learn, Flask)
- **Machine Learning** (Random Forest Regressor)
- **Data Preprocessing** (Handling missing values, feature selection)
- **Web Development** (Flask for user interface)

---
## Future Improvements
🔹 Add more features (e.g., sleep patterns, stress levels)  
🔹 Improve model accuracy with **hyperparameter tuning**  
🔹 Deploy on **AWS/GCP/Heroku** for online access  

---
## Contributing
Feel free to fork this repo, make changes, and submit a pull request. Contributions are welcome!

---
## License
MIT License © 2025 Ashok Kumar S
