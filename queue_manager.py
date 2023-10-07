from collections import deque
import time

class QueueManager:
    def __init__(self):
        self.queue = deque()
        self.time_stamps = deque()

    def add_to_queue(self, request):
        current_time = time.time()

        # Remove outdated timestamps
        while self.time_stamps and self.time_stamps[0] < current_time - 3600:
            self.time_stamps.popleft()

        # Check rate limit (assuming 1000 requests/hour)
        if len(self.time_stamps) < 1000:
            self.queue.append(request)
            self.time_stamps.append(current_time)
        else:
            print("Rate limit exceeded. Please wait.")
