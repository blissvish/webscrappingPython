import requests
API_ENDPOINT = "http://api.hackerrank.com/checker/submission.json"
API_KEY = "hackerrank|"
#generate your own api key and copy paste here

address = input("Relative address of the source code python file: ")

with open(address,'r') as myfile:
        data1 = myfile.read()

query = {"source" : data1,"lang" : '5',"testcases" : '["1"]',"api_key" : API_KEY,"wait" :  'false',"callback_url" : '',"format": 'json'}

r = requests.post ( url = API_ENDPOINT, data = query)
if r.json()['result']['stderr'][0] == False:
        print(r.json()['result']['stdout'][0])
else:
        print("Error")
