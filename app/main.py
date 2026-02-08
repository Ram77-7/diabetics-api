from fastapi import FastAPI,HTTPException,Depends
from app.schemas import Symptoms
from app.predict import predict_diabetes
from app.dependencies import get_db
from app.db_models import DiabeticsPrediction
from sqlalchemy.orm import Session

app = FastAPI(
    title="Diabetes Prediction API",
    description="API to predict diabetes using machine learning model",
    version="1.0"
)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

@app.post("/predict")
def predict(input_data: Symptoms, db:Session =Depends(get_db)):
    try:
        # ML Prediction
        result = predict_diabetes(input_data)
        if hasattr(result, "item"):
            result = result.item()

        # Save to DB
        record = DiabeticsPrediction(
            Pregnancies=input_data.Pregnancies,
            Glucose=input_data.Glucose,
            BloodPressure=input_data.BloodPressure,
            SkinThickness=input_data.SkinThickness,
            Insulin=input_data.Insulin,
            BMI=input_data.BMI,
            DiabetesPedigreeFunction=input_data.DiabetesPedigreeFunction,
            Age=input_data.Age,
            Prediction = result
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return {
            "prediction": str(result),
            "record_id": record.id
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))