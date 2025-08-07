import yaml

def load_rules(path='rules/basic_keyword_rules.yaml'):
    with open(path) as f:
        return yaml.safe_load(f).get("keywords", [])

def detect_anomalies(log_lines, keywords):
    return [line for line in log_lines if any(kw in line for kw in keywords)]
