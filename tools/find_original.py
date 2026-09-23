import json, os

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        tool_calls = data.get('tool_calls') or []
        for tc in tool_calls:
            name = tc.get('name')
            params = tc.get('parameters', {})
            path = params.get('AbsolutePath') or params.get('TargetFile') or ''
            if 'index.html' in path or 'index' in path:
                print(f"Step {idx} [{data.get('type')}]: {name} -> {path}")
