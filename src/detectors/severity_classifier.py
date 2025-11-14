thonclass SeverityClassifier:
    def classify(self, message: str) -> str:
        msg_lower = message.lower()
        if "critical" in msg_lower or "panic" in msg_lower or "fatal" in msg_lower:
            return "critical"
        elif "error" in msg_lower or "failed" in msg_lower:
            return "high"
        elif "warn" in msg_lower or "deprecated" in msg_lower:
            return "medium"
        else:
            return "low"