import pandas as pd

# Load dataset
file_path = r"C:\Users\lenovo\OneDrive\Documents\DS Mini Final\student.csv"  # Update with correct path
df = pd.read_csv(file_path)

# Columns to remove (update this list based on your dataset)
unwanted_columns = ['Age', 'Gender', 'Ethnicity', 'Sports', 'Music', 'Volunteering', 'ParentalEducation', 'GradeClass']
df = df.drop(columns=[col for col in unwanted_columns if col in df.columns], errors='ignore')

# Normalize GPA to range 0-10
if 'GPA' in df.columns:
    max_gpa = df['GPA'].max()
    if max_gpa > 0:
        df['GPA'] = (df['GPA'] / max_gpa) * 10  # Scale max value to 10
    df['GPA'] = df['GPA'].round(2)  # Round to 2 decimal places

# Convert 'StudyHours' to 3 decimal float
if 'StudyHours' in df.columns:
    df['StudyHours'] = df['StudyHours'].astype(float).round(3)

# Handle missing values (choose one method)
df = df.dropna()  # Option 1: Remove rows with missing values
# df.fillna(df.mean(), inplace=True)  # Option 2: Fill missing values with column mean

# Save cleaned dataset
cleaned_file_path = r"C:\Users\lenovo\OneDrive\Documents\DS Mini Final\cleaned_student.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"✅ Data cleaned and saved to: {cleaned_file_path}")
