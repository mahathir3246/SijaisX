import requests

url = "http://127.0.0.1:5000/api/school"   # include /api/school
payload = {"school_name": "Jokiniemen Koulu"}

try:
    resp = requests.post(url, json=payload, timeout=5)
    print("status:", resp.status_code)      # 201 means “created”
    print("body  :", resp.json())           # {"message": "Insertion successful"}
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
