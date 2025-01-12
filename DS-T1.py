import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def data_pipeline(file_path):
    # Step 1: Load Data
    print("Loading data...")
    data = pd.read_csv(file_path)
    print("Data loaded successfully.")

    # Step 2: Drop Unnecessary Columns
    print("Dropping unnecessary columns...")
    data = data.drop(columns=["id", "name"])  
    print("Unnecessary columns dropped.")

    # Step 3: Handle Missing Values
    print("Handling missing values...")
    data["income"] = data["income"].fillna(data["income"].mean())

    print("Missing values handled.")

    # Step 4: Encode Categorical Variables
    print("Encoding categorical variables...")
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        label_encoders[column] = LabelEncoder()
        data[column] = label_encoders[column].fit_transform(data[column])
    print("Categorical variables encoded.")

    # Step 5: Feature Scaling
    print("Scaling features...")
    scaler = StandardScaler()
    features = data.drop("target", axis=1)  # Separate features and target
    target = data["target"]
    features_scaled = scaler.fit_transform(features)
    print("Features scaled.")

    # Step 6: Train-Test Split
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        features_scaled, target, test_size=0.2, random_state=42)
    print("Data split successfully.")

    return X_train, X_test, y_train, y_test

# Example usage
if __name__ == "__main__":
    # Ensure `data.csv` is in the same directory as this script
    X_train, X_test, y_train, y_test = data_pipeline("data.csv")
    print("Pipeline execution complete.")
