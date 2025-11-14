thonimport json
from pathlib import Path
from datetime import datetime
from extractors.problem_parser import ProblemParser
from extractors.context_utils import extract_context
from outputs.exporters import export_json

def load_settings():
    config_path = Path(__file__).parent / "config" / "settings.example.json"
    with open(config_path, "r") as f:
        return json.load(f)

def run():
    settings = load_settings()
    input_path = Path(settings.get("input_path", "data/sample_input.txt"))
    output_path = Path(settings.get("output_path", "data/sample_output.json"))

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    parser = ProblemParser()

    results = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            parsed = parser.parse_line(line.strip())
            if parsed:
                parsed["context"] = extract_context(line)
                parsed["timestamp"] = datetime.utcnow().isoformat() + "Z"
                results.append(parsed)

    export_json(results, output_path)
    print(f"[OK] Parsed {len(results)} problem messages → {output_path}")

if __name__ == "__main__":
    run()