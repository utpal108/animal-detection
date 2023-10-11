from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from animalDetection.utils.common import decodeImage
from animalDetection.pipeline.predict import PredictionPipeline
from animalDetection.config.configuration import ConfigurationManager


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        filename = 'inputImage.jpg'
        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        self.filename = os.path.join(prediction_config.root_dir,filename)
        self.classifier = PredictionPipeline(self.filename)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system('dvc repro')
    return 'Training done successfully'

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True) # For Local Host