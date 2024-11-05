import sys
import requests
import json

api_url: str = 'https://ssd.jpl.nasa.gov/api/horizons_file.api'

request_id: str = sys.argv[1]
request_file_dir: str = 'requests/{}'.format(request_id)
request_file = open(request_file_dir)

print("sending request to JPL Horizons")
post_request = requests.post(api_url, data={'format':'json'}, files={'input': request_file})
response = json.loads(post_request.text)

print("received response, parsing the result")
result: str = response["result"]

print("writing result to file")
result_file_dir: str = "results/{}.result".format(request_id)
result_file = open(result_file_dir, "w")
result_file.write(result)
result_file.close()

post_request.close()
print("request complete\nresult has been written to the file named:\n{}".format(result_file_dir))
