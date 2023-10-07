import requests
from queue_manager import QueueManager

def fetch_data():
    try:
        # Initialize Queue Manager for rate-limiting
        queue = QueueManager()

        # Fetch data from fake FEC API
        queue.add_to_queue("https://fake-fec-api.example.com/data")
        response = requests.get("https://fake-fec-api.example.com/data")

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except Exception as e:
        print(f"API Error: {e}")
