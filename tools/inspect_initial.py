import json

log_file = r'C:\Users\Camila\.gemini\antigravity-ide\brain\2a0e1f7f-07b5-473b-ac20-a586ddf02103\.system_generated\logs\transcript_full.jsonl'

with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if idx <= 45:
            data = json.loads(line)
            # check if there's any file view or content
            print(f"Step {idx}: type={data.get('type')}, source={data.get('source')}")
            for tc in (data.get('tool_calls') or []):
                print(f"   Tool: {tc.get('name')}, params: {tc.get('parameters')}")
            if data.get('type') == 'USER_INPUT':
                print(f"   User message: {str(data.get('content'))[:150]}")
