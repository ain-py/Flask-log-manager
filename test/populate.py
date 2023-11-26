import json
from anyio import sleep
import requests
import random
import string
url = "http://127.0.0.1:3000/add_log"


for i in range(0,10):
    # sleep(0.001)
    message = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=7))
    level = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=4))
    traceId = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=3))
    resourceId = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=3))
    prId = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=2))
    data ={
        "level": str(level),
        "message": str(message),
        "resourceId": f"server-{resourceId}",
        "timestamp": "2023-09-15T08:00:00Z",
        "traceId": f"abc-{traceId}-123",
        "spanId": f"span-{level}",
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": f"server-{prId}"
        }
    }
    payload = json.dumps(data)
    print(payload)
    

    response = requests.request("POST", url, data={"log_data": str(payload)})

    print(response.text)
