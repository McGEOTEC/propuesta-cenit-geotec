import sqlite3, json

db_path = r'C:\Users\Camila\.gemini\antigravity-ide\conversations\2a0e1f7f-07b5-473b-ac20-a586ddf02103.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT step_index, source, type, content, tool_calls FROM steps;")
rows = cursor.fetchall()
print('Total steps:', len(rows))

for r in rows:
    step_idx, source, stype, content, tool_calls = r
    # check if content or tool_calls has '<!DOCTYPE html>'
    s_content = str(content or '')
    s_tc = str(tool_calls or '')
    if '<!DOCTYPE html>' in s_content:
        print(f"Step {step_idx} content has DOCTYPE, length: {len(s_content)}")
    if '<!DOCTYPE html>' in s_tc:
        print(f"Step {step_idx} tool_calls has DOCTYPE, length: {len(s_tc)}")

conn.close()
