Esta solución permite predecir la popularidad de canciones basado en las variables propias de la cancion como son:
    'duration_ms': fields.Float(required=False, description='Duration of the track in milliseconds'),
    'danceability': fields.Float(required=False, description='Danceability score'),
    'energy': fields.Float(required=False, description='Energy score'),
    'loudness': fields.Float(required=False, description='Loudness level'),
    'speechiness': fields.Float(required=False, description='Speechiness score'),
    'acousticness': fields.Float(required=False, description='Acousticness score'),
    'instrumentalness': fields.Float(required=False, description='Instrumentalness score'),
    'liveness': fields.Float(required=False, description='Liveness score'),
    'valence': fields.Float(required=False, description='Valence score'),
    'tempo': fields.Float(required=False, description='Tempo (BPM)'),
    'explicit': fields.Integer(required=False, description='Explicit flag (Use 0 for False or 1 for True)'),
    'mode': fields.Integer(required=False, description='Mode (0 or 1)'),
    'time_signature': fields.Integer(required=False, description='Time signature'),

La solución es una API que se compone de los siguientes archivos:
api_popularity.py: Es la interfaz de la API la cual puede ser ejecutada a traves de HTTP con un metodo POST, invocando el JSON con los parametros descritos arriba. Como respuesta se tendra el valor de predicción de la respuesta que esta entre 0 y 100
predic_popularity.py: Este archivo se encarga de hacer el tratamiento de los datos, como son la codificación y estandarización de las variables, una vez se realiza este proceso invoca al modelo entrenado para hacer la predicción.
trackspopularity_clf.pkl: Este es el modelo entrenado empaquetado el cual se debe desplegar con toda la solución.
requirements.txt: Este es el archivo con los requerimientos para instalar la solución. 
