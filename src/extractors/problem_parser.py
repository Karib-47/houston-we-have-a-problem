thonimport re

class ProblemParser:
    """
    Detects error/problem lines and extracts basic metadata.
    """

    SEVERITY_MAP = {
        "critical": ["critical", "fatal", "panic", "severe"],
        "warning": ["warn", "caution", "alert"],
        "info": ["info", "notice"]
    }

    def detect_severity(self, text: str) -> str:
        text_lower = text.lower()
        for level, keywords in self.SEVERITY_MAP.items():
            if any(kw in text_lower for kw in keywords):
                return level
        return "unknown"

    def parse_line(self, line: str):
        if not line:
            return None

        # Detect common problem keywords
        problem_keywords = ["error", "fail", "problem", "exception", "crash"]
        if not any(kw in line.lower() for kw in problem_keywords):
            return None

        severity = self.detect_severity(line)

        return {
            "message": line,
            "severity": severity,
            "source": "system-log"
        }