thonimport json
import csv
import os

class ReportGenerator:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def generate(self, problems):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        json_path = self.output_path
        csv_path = os.path.splitext(self.output_path)[0] + ".csv"

        # Write JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(problems, f, indent=2)

        # Write CSV
        if problems:
            keys = problems[0].keys()
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(problems)