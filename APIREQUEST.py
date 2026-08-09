import requests

payload="data"
json={'key':12,'key2':1}
response=requests.get("url")
requests.post("url",data=payload)
requests.post("url",json=json,headers="header data")
response.headers
response.raise_for_status
response.json()
