# # source venv/bin/activate

import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
model = tf.keras.models.load_model('/Users/rdi/Desktop/my_cs445_model.h5')

map = {5: 'nv', 4: 'mel', 2: 'bkl', 1: 'bcc', 0: 'akiec', 6: 'vasc', 3: 'df'}

@app.route('/')
def index():
    return render_template('page.html') 

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        image = Image.open(io.BytesIO(file.read()))
        image = image.resize((227, 227))
        image = np.array(image)
        image = image / 255.0
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image)
        prediction = np.array(prediction)
        large_index = np.argmax(prediction)
        print(large_index)
        result = map.get(large_index)
        print(result)
        response = {'Disease': str(result)}
        return jsonify(response)
    
if __name__ == '__main__':
    app.run()
