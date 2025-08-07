import json

def parse_syslog(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse_json_log(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
