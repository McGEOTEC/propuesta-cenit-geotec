import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if idx in [33, 35, 37, 39]:
            data = json.loads(line)
            print(f"=== Step {idx} ===")
            content = data.get('content', '')
            print(content[:1500].encode('ascii', 'replace').decode('ascii'))
