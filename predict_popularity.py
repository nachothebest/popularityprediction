import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler

def predecir_popularidad(input_data):
    # Cargar modelo y scaler (asegúrate de guardar y cargar scaler si es necesario)
    modelo_path = os.path.join(os.path.dirname(__file__), 'trackspopularity_clf.pkl')
    mejor_modelo = joblib.load(modelo_path)

    # Variables esperadas
    numeric_cols = ['duration_ms', 'danceability', 'energy', 'loudness', 'speechiness',
                    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    low_card_cat = ['explicit', 'mode', 'time_signature']

    # Crear DataFrame con 1 fila
    df_input = pd.DataFrame([input_data])

    # Rellenar faltantes con medias o valores por defecto
    for col in numeric_cols:
        if col not in df_input.columns:
            df_input[col] = 0  # O podrías usar una media estimada

    for col in low_card_cat:
        if col not in df_input.columns:
            df_input[col] = 0  # Supón categoría más común o 0

    # One-hot encoding, asegurarse de que tenga todas las columnas necesarias
    df_input = pd.get_dummies(df_input, columns=low_card_cat, drop_first=True)

    # Asegurar que las columnas estén alineadas con las del modelo
    expected_cols = mejor_modelo.feature_names_in_  # Esto da las columnas esperadas por XGBoost
    for col in expected_cols:
        if col not in df_input.columns:
            df_input[col] = 0  # Añadir columnas faltantes como 0
    
    df_input = df_input[expected_cols]

    # Escalar numéricas (si tienes un scaler guardado)
    # scaler = joblib.load('scaler.pkl')
    # df_input[numeric_cols] = scaler.transform(df_input[numeric_cols])

    # Predicción
    prediccion = mejor_modelo.predict(df_input)[0]

    return prediccion

# Uso desde consola
if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) == 1:
        print('Por favor ingresa un JSON con los datos del track.')
    else:
        input_json = sys.argv[1]
        input_data = json.loads(input_json)

        pred = predecir_popularidad(input_data)
        print(f'Predicción de popularidad: {pred:.2f}')