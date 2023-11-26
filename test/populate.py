import json
from anyio import sleep
import random
from datetime import datetime, timedelta
import requests
import random
import string
url = "http://127.0.0.1:3000/add_log"


for i in range(0,1):
    # sleep(0.001)
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 1, 1)

    random_datetime = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

    formatted_datetime = random_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

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
        "timestamp": formatted_datetime,
        "traceId": f"abc-{traceId}-123",
        "spanId": f"span-{level}",
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": f"server-{prId}"
        }
    }
    payload = json.dumps(data)
    response = requests.request("POST", url, data={"log_data": str(payload)})
    print(payload)
    print(response.text)
