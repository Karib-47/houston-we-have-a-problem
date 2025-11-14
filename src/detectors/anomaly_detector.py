thonimport hashlib
import time

class AnomalyDetector:
    def __init__(self, threshold: int = 3):
        self.threshold = threshold

    def detect(self, logs):
        problem_list = []
        seen_messages = {}
        for line in logs:
            msg_hash = hashlib.md5(line.encode()).hexdigest()
            seen_messages[msg_hash] = seen_messages.get(msg_hash, 0) + 1

            if "error" in line.lower() or "fail" in line.lower() or seen_messages[msg_hash] > self.threshold:
                problem_list.append({
                    "problem_id": msg_hash[:8],
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "source": "system",
                    "message": line,
                    "status": "open"
                })
        return problem_list