import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        if idx in [32, 34, 36, 38]:
            print(f"=== STEP {idx} ===")
            print(json.dumps(data.get('tool_calls'), indent=2))
