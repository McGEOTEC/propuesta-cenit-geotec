import json, re

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        line_str = json.dumps(data)
        if 'PROPUESTA_CENIT' in line_str:
            # find what files were mentioned
            matches = re.findall(r'[a-zA-Z0-9_\-\\]+\.(?:html|py|js|css|json|md)', line_str)
            if matches:
                unique_m = list(set(matches))
                print(f"Step {idx}: {unique_m[:6]}")
