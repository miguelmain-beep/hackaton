import pandas as pd
from sklearn.linear_model import LogisticRegression
# import numpy as np

class MLService:
    def __init__(self):
        # Aquí se cargarían los modelos preentrenados (ej. usando joblib)
        self.model = LogisticRegression()
    
    def predecir_accidente(self, latitud, longitud, clima):
        # Lógica dummy
        return 0.85

ml_service = MLService()
