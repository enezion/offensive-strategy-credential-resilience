import json
import re

def generate_report(log_file):
    findings = []
    pattern = r"ACCOUNT FOUND: \[(.*?)\] User: (.*?) - Pass: (.*?) \[SUCCESS\]"
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                findings.append({
                    "host": match.group(1),
                    "user": match.group(2),
                    "pass": match.group(3),
                    "risk": "CRITICAL"
                })
                
    with open('reports/audit_results.json', 'w') as out:
        json.dump({"summary": "Relatório Técnico", "data": findings}, out, indent=4)

# generate_report('medusa_output.txt')
