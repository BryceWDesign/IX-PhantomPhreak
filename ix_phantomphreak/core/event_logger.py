"""
IX-PhantomPhreak Event Logger

Records detailed logs of all detected exploit attempts, including timestamp,
input payload, and detection metadata. Supports retrieval and export.
"""

import time
from typing import List, Dict

class EventLogger:
    def __init__(self):
        self.logs: List[Dict] = []

    def log_event(self, source: str, input_text: str, detected_patterns: List[str]):
        event = {
            "timestamp": time.time(),
            "source": source,
            "input": input_text,
            "patterns_detected": detected_patterns
        }
        self.logs.append(event)

    def get_recent_events(self, count: int = 10):
        return self.logs[-count:]

    def export_logs(self, filepath: str):
        import json
        with open(filepath, "w") as f:
            json.dump(self.logs, f, indent=4)

# Example usage
if __name__ == "__main__":
    logger = EventLogger()
    logger.log_event("IX-Joey", "DROP TABLE users;", ["DROP TABLE"])
    print("Recent events:", logger.get_recent_events())
