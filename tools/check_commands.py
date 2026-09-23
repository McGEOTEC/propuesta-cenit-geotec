import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        if idx in [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 58, 59, 60, 61, 62, 63, 64]:
            t = data.get('type')
            tc = data.get('tool_calls')
            cmd = ''
            if tc:
                for c in tc:
                    if c.get('name') == 'run_command':
                        cmd = c.get('parameters', {}).get('CommandLine', '')
            print(f"Step {idx}: type={t}, cmd={cmd[:80]}")
