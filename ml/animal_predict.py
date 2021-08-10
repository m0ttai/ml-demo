import io
import json
from flask import Flask, jsonify, request
from PIL import Image
import glob
from google.cloud.storage import bucket, client
import numpy as np
import tensorflow
import tensorflow as tf
from google.cloud import storage as gcs
from google.oauth2 import service_account

app = Flask(__name__)

'''
def return_predict():
	input_image = Image.open(image_file[0])
	input_image = input_image.convert('RGB')
	input_image = input_image.resize((100, 100))
	input_image = np.asarray(input_image)
	X = []
	X.append(input_image)
	X = np.array(X)
	results = model.predict([X])[0]
	# result = int(results[results.argmax()] * 100)
	return results

results = return_predict()
# print(image_file, ': {0}'.format(class_label[results.argmax()], result))
print(image_file, ': {0}'.format(class_label[results.argmax()]))
print(results)

@app.route('/', methods=['POST'])
def return_predict():
	model = tensorflow.keras.models.load_model('/data/ml/model.h5')
	image_path = '/data/ml/images/'
	image_file = glob.glob(image_path + 'cat.jpg')
	class_label = ('cat', 'crow', 'horse', 'lion', 'turtle')

	input_image = Image.open(image_file[0])
	input_image = input_image.convert('RGB')
	input_image = input_image.resize((100, 100))
	input_image = np.asarray(input_image)
	X = []
	X.append(input_image)
	X = np.array(X)

	results = model.predict([X])[0]
	return jsonify({"message": "This is the {}.".format(class_label[results.argmax()])})
'''

@app.route('/', methods=['POST'])
def return_predict():
	# Variables
	gcs_project_id = 'direct-plateau-322502'
	gcs_key_path = '/config/cka-project-318105-d0bd042b7921.json'
	gcs_bucket_name = 'yu1-ml-demo'
	class_label = ('cat', 'crow', 'horse', 'lion', 'turtle')
	model_path = '/model.h5'
	model = tf.keras.models.load_model(model_path)
	X = []

	# Get Request
	req = json.loads(request.json)

	# Get Image File
	gcs_client = gcs.Client(gcs_project_id, credentials=service_account.Credentials.from_service_account_file(gcs_key_path))
	gcs_bucket = gcs_client.get_bucket(gcs_bucket_name)
	predict_file = gcs_bucket.get_blob(req['file_name'])

	# Retouch & Convert Image File
	input_file = Image.open(io.BytesIO(predict_file.download_as_string()))
	input_file = input_file.convert('RGB')
	input_file = input_file.resize((100, 100))
	input_file = np.asarray(input_file)
	X.append(input_file)
	X = np.array(X)

	# Predict Image File
	results = model.predict([X])[0]

	# Set Object's Metadata
	gcs_metadata = {'class': class_label[results.argmax()]}
	predict_file.metadata = gcs_metadata
	predict_file.patch()
	# return jsonify({"message": "This is the {}.".format(class_label[results.argmax()])})
	return jsonify({"message": "{} is {}".format(predict_file.name, predict_file.metadata)})

# @app.route('/', methods=['POST'])
# def return_message():
# 	return jsonify({"message": "Hello!!"})

# def return_message():
# 	request_data = request.get_json()
# 	# return jsonify({"message": "Thanks Request. Parameter is {}".format(request_data["file"])})
# 	return request_data["file"]

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=80)