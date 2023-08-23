from pydantic import BaseModel


class WaterPotability(BaseModel):
    """
    --Represents a on the Water potability with various attributes.

    Attributes:
       aqui van los atributos del data set excepto la variable onjetivo
    """

    ph: float
    Hardness: float
    Solids: float
    Chloramines: int
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float
