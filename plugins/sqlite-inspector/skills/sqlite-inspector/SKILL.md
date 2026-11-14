---
name: sqlite-inspector
description: Inspect SQLite databases, dump table schemas, run diagnostic queries, verify Room database migrations, and export data using Python's native sqlite3 engine. Use when querying local .db/.sqlite files, inspecting Android app databases, or debugging relational models.
tools: Read, Glob, Grep, Bash
---

# SQLite Inspector

Autonomous SQLite database explorer and schema validator using Python's native `sqlite3` library (zero external dependencies).

## Directives
- **Read-Only by Default**: Use `PRAGMA query_only = ON;` unless mutation is explicitly requested.
- **Parametric Execution**: Prevent SQL injection risks in generated scripts.
- **Android App DB Pull**: When inspecting an Android app's internal database, pull it to the dedicated sandbox first via ADB:
  ```bash
  adb shell "cp /data/data/<pkg>/databases/<db_name> /storage/emulated/0/Antigravity/песочница/<db_name>"
  ```

---

## Common Inspector Commands

### 1. Schema & Table Summary
Run a one-liner to dump all tables and column schemas:
```bash
python -c "
import sqlite3, sys
conn = sqlite3.connect('path/to/database.db')
cursor = conn.cursor()
cursor.execute(\"SELECT name, sql FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%';\")
for name, sql in cursor.fetchall():
    print(f'=== TABLE: {name} ===\n{sql}\n')
conn.close()
"
```

### 2. Sample Data Inspection
```bash
python -c "
import sqlite3
conn = sqlite3.connect('path/to/database.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM table_name LIMIT 10;')
cols = [desc[0] for desc in cursor.description]
print(' | '.join(cols))
print('-' * 40)
for row in cursor.fetchall():
    print(' | '.join(str(val) for val in row))
conn.close()
"
```

### 3. Row Counts & Integrity Check
```bash
python -c "
import sqlite3
conn = sqlite3.connect('path/to/database.db')
cursor = conn.cursor()
cursor.execute('PRAGMA integrity_check;')
print('Integrity:', cursor.fetchone()[0])
cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';\")
for (t,) in cursor.fetchall():
    cursor.execute(f'SELECT count(*) FROM {t};')
    print(f'{t}: {cursor.fetchone()[0]} rows')
conn.close()
"
```
