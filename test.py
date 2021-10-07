import os
import requests

url = 'https://api.github.com/gists/{}'.format(os.environ.get('gist_id'))
message, color, value = os.environ.get('message'), os.environ.get('color'), os.environ.get('value')
string_json = '{"schemaVersion": 1, "label": "%s", "message": "%s", "color": "%s"}' % (message, value, color)

print(os.environ)
print(url, message, color, value, string_json)

myobj = {"public": False, "files": {"coverage.json": {"content": string_json}}}

x = requests.patch(url, json=myobj, auth=('loicdiridollou', os.environ.get('secret')))

print(x.text)