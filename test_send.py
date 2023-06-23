import requests

f = open("data.txt","r")
data = f.read()
batch = 5

url = "http://localhost:8000/predict"

payload = {
    "data":[
        {"image":data},
        {"image":data},
        {"image":data}
    ]
}
headers = {}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
