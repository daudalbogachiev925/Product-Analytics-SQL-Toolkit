import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("analytics.db")
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS events;
CREATE TABLE events (
  user_id INTEGER,
  event TEXT,
  ts TEXT
);
""")

events = ["signup", "activate", "purchase", "churn"]
now = datetime.now()
rows = []
for uid in range(1, 501):
    t0 = now - timedelta(days=random.randint(0, 60))
    rows.append((uid, "signup", t0.isoformat()))
    if random.random() > 0.3:
        rows.append((uid, "activate", (t0 + timedelta(hours=2)).isoformat()))
    if random.random() > 0.6:
        rows.append((uid, "purchase", (t0 + timedelta(days=1)).isoformat()))
cur.executemany("INSERT INTO events VALUES (?,?,?)", rows)
conn.commit()
conn.close()
print("Seeded analytics.db")
