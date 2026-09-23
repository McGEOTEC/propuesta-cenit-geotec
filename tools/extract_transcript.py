import json
import re

tpath = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'
with open(tpath, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '89768' in line:
            print(f"Match on line {i}")
            obj = json.loads(line)
            print("Keys:", obj.keys())
            # check content
            if 'content' in obj:
                print("Content len:", len(str(obj['content'])))
                print(str(obj['content'])[:500])
