import joblib 
from sklearn.linear_model import LogisticRegression

Load_model = joblib.load("app/models/model (2).pkl")

print("Model loaded successfully.")
