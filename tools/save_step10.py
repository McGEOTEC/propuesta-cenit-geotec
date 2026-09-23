import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if idx == 10:
            data = json.loads(line)
            c = data.get('content', '')
            with open('original_readme_step10.txt', 'w', encoding='utf-8') as out:
                out.write(c)
            print('Saved step 10 to original_readme_step10.txt, length:', len(c))
