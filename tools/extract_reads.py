import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if idx < 65:
            data = json.loads(line)
            c_txt = str(data.get('content') or '')
            if 'index.html' in c_txt or '<!DOCTYPE' in c_txt:
                print(f"=== Step {idx} (type: {data.get('type')}) ===")
                lines = c_txt.split('\n')
                for l in lines[:20]:
                    print("  ", l[:120])
