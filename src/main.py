thonimport json
import os
from detectors.anomaly_detector import AnomalyDetector
from detectors.severity_classifier import SeverityClassifier
from outputs.report_generator import ReportGenerator

def load_logs(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def load_settings():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'settings.example.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    settings = load_settings()
    logs = load_logs(settings['input_logs_path'])
    detector = AnomalyDetector(threshold=settings['anomaly_threshold'])
    classifier = SeverityClassifier()
    report_gen = ReportGenerator(settings['output_path'])

    print("[INFO] Starting anomaly detection...")
    problems = detector.detect(logs)

    print("[INFO] Classifying detected problems...")
    for problem in problems:
        problem['severity'] = classifier.classify(problem['message'])

    print(f"[INFO] {len(problems)} problems detected. Generating report...")
    report_gen.generate(problems)
    print(f"[INFO] Report generated at: {settings['output_path']}")

if __name__ == "__main__":
    main()