import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if idx in [4, 6, 26, 28, 30, 32, 33, 34]:
            data = json.loads(line)
            print(f"Step {idx}: {data.get('type')}")
            content = data.get('content')
            if content:
                print(str(content)[:500])
