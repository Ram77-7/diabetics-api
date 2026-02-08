from sqlalchemy import Column,Integer,Float,String,DateTime
from datetime import datetime
from app.database import Base

class DiabeticsPrediction(Base):
    __tablename__ = "diabetics_prediction"
    id = Column(Integer, primary_key=True, index=True)
    Pregnancies = Column("Pregnancies", Integer)
    Glucose = Column("Glucose", Integer)
    BloodPressure = Column("BloodPressure", Integer)
    SkinThickness = Column("SkinThickness", Integer)
    Insulin = Column("Insulin", Integer)
    BMI = Column("BMI", Float)
    DiabetesPedigreeFunction = Column("DiabetesPedigreeFunction", Float)
    Age = Column("Age", Integer)
    Prediction = Column(String)
    created_at = Column(DateTime,default=datetime.utcnow)
