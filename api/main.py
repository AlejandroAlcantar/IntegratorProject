
import os
import sys

from fastapi import FastAPI
from starlette.responses import JSONResponse

from api.models.models import WaterPotability
from integratorproject.integratorproject.Predictor.predict import \
    ModelAPIPredictor
from integratorproject.integratorproject.utilities.custom_loggin import \
    CustomLogging

logger = CustomLogging()
logger = logger.CreateLogger(file_name='main.log')

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(current_dir)

relative_path = "integratorproject\\integratorproject\\models"
model_path = os.path.join(os.path.abspath(parent_dir), relative_path)

app = FastAPI()

"""
PARAMETER VALUES
Values are required after de endpoint.
"""


@app.get('/', status_code=200)
async def healthcheck():
    return 'WaterPotability Regressor is ready to go!'


@app.post('/predict')
def predictor(waterpotability_features: WaterPotability):
    predictor = ModelAPIPredictor(
        model_path + "\\logistic_regression_output.pkl")
    X = [
        waterpotability_features.ph,
        waterpotability_features.Hardness,
        waterpotability_features.Solids,
        waterpotability_features.Chloramines,
        waterpotability_features.Sulfate,
        waterpotability_features.Conductivity,
        waterpotability_features.Organic_carbon,
        waterpotability_features.Trihalomethanes,
        waterpotability_features.Turbidity
    ]
    prediction = predictor.predict([X])
    logger.info("perdiction was made correctly")
    return JSONResponse(f"Resultado predicción: {prediction}")
