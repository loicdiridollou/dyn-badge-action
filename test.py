import os
import requests

url = 'https://api.github.com/gists/{}'.format(os.environ.get('INPUT_gist_id')  )
message, color, value = os.environ.get('INPUT_message'), os.environ.get('INPUT_color'), os.environ.get('INPUT_value')
string_json = '{"schemaVersion": 1, "label": "%s", "message": "%s", "color": "%s"}' % (message, value, color)

myobj = {"public": False, "files": {"coverage.json": {"content": string_json}}}

x = requests.patch(url, json=myobj, auth=('loicdiridollou', os.environ.get('INPUT_secret')))

print(x.text)