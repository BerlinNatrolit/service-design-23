import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(api_url, json=todo)

print(response.json())
# {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code)
    # 201

if(response):
    if(response.status_code == 200):
        print("we are now in status_code specific")
    print("this worked")