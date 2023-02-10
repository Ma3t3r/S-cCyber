import requests

url = "http://www.example.com/api/get_data"

# O ID que você quer testar
for i in range(100):
    headers = {
        "Content-Type": "application/json",
    }
    data = {"id": str(i)}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"ID válido encontrado: {i}")
        break
