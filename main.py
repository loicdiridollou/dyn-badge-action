"""
Module to update the content of the gist json that defines the badge (badge
defined by the user using the gist_id argument
"""
import os
import requests

# labelling target URL
url = 'https://api.github.com/gists/{}'.format(os.environ.get('INPUT_GIST_ID'))

# getting the values for message, color and number
message, color, value = os.environ.get('INPUT_MESSAGE'), os.environ.get('INPUT_COLOR'), os.environ.get('INPUT_VALUE')

# preparing the string to be updated in the gist file
string_json = '{"schemaVersion": 1, "label": "%s", "message": "%s", "color": "%s"}' % (message, value, color)

# preparing the data to be included in the request
req_data = {"public": False, "files": {os.environ.get('INPUT_FILENAME'): {"content": string_json}}}

# performing the patch request
req = requests.patch(url, json=req_data, auth=(os.environ.get('INPUT_USER'), os.environ.get('INPUT_SECRET')))
