from flask import Flask
from flask_restx import Api, Resource, fields

from predict_popularity import predecir_popularidad



app = Flask(__name__)

# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='Music Popularity Prediction API',
    description='Predict popularity of music tracks based on audio features.'
)

ns = api.namespace('predict', description='Popularity Prediction Endpoint')

# Definición argumentos o parámetros de la API (JSON input expected)
input_fields = api.model('TrackFeatures', {
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
})

# Output definition
resource_fields = api.model('PredictionResult', {
    'result': fields.Float(description='Predicted popularity score'),
})

# Definición de la clase para disponibilización
@ns.route('/')
class PopularityApi(Resource):

    @ns.expect(input_fields)
    @ns.marshal_with(resource_fields)
    def post(self):
        input_data = api.payload  # JSON input
        predicted_score = predecir_popularidad(input_data)
        
        return {
            "result": predicted_score
        }, 200
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5002)
