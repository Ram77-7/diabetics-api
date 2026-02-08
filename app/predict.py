from app.model import Load_model  # Your pre-trained ML model
import numpy as np
from fastapi import HTTPException

def predict_diabetes(input_data):
    try:
        X = np.array([[
            input_data.Pregnancies,
            input_data.Glucose,
            input_data.BloodPressure,
            input_data.SkinThickness,
            input_data.Insulin,
            input_data.BMI,
            input_data.DiabetesPedigreeFunction,
            input_data.Age
        ]], dtype=float)

        prediction = Load_model.predict(X)[0]

        # Return string directly
        return "positive" if prediction == 1 else "negative"

    except Exception as e:
        print("DIABETES PREDICTION ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
