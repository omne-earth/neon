import sys
import requests
import json

request_id: str = sys.argv[1]
request_file_dir: str = 'requests/{}'.format(request_id)
request_file = open(request_file_dir)

api_url: str = 'https://ssd.jpl.nasa.gov/api/horizons_file.api'
post_request = requests.post(api_url, data={'format':'json'}, files={'input': request_file})

response = json.loads(post_request.text)
result: str = response["result"]
result_file = open("results/{}.result".format(request_id), "w")
result_file.write(result)
result_file.close()

post_request.close()
