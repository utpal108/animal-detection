import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from animalDetection.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self,filename):
        self.config = ConfigurationManager()
        self.filename = filename

    def predict(self):
        trained_model_config = self.config.get_training_config()
        
        # load model
        model = load_model(trained_model_config.trained_model_path)

        # Input image file from UI
        image_name = self.filename
        test_image = image.load_img(image_name, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 0:
            prediction = 'Cat'
            return [{'image' : prediction}]
        else:
            prediction = 'Dog'
            return [{'image' : prediction}]