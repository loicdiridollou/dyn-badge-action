import os
import requests

url = 'https://api.github.com/gists/{}'.format(os.environ.get('INPUT_GIST_ID'))
message, color, value = os.environ.get('INPUT_MESSAGE'), os.environ.get('INPUT_COLOR'), os.environ.get('INPUT_VALUE')
string_json = '{"schemaVersion": 1, "label": "%s", "message": "%s", "color": "%s"}' % (message, value, color)

myobj = {"public": False, "files": {"coverage.json": {"content": string_json}}}

x = requests.patch(url, json=myobj, auth=(os.environ.get('INPUT_USER'), os.environ.get('INPUT_SECRET')))

print(x.text)