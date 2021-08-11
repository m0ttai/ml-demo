# import requests
# from google.cloud import storage as gcs

def gcs_change_log(data, context):
	print('Event ID: {}'.format(context.event_id))
	print('Event type: {}'.format(context.event_type))
	print('Bucket: {}'.format(data['bucket']))
	print('File: {}'.format(data['name']))
	print('Metageneration: {}'.format(data['metageneration']))
	print('Created: {}'.format(data['timeCreated']))
	print('Updated: {}'.format(data['updated']))
	return 'Done!'