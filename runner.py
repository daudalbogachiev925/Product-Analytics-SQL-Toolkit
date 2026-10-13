import sqlite3, sys, pathlib

def run(sql_file):
    conn = sqlite3.connect("analytics.db")
    sql = pathlib.Path(sql_file).read_text(encoding="utf-8")
    cur = conn.execute(sql)
    cols = [d[0] for d in cur.description]
    print("\t".join(cols))
    for row in cur.fetchall():
        print("\t".join(str(x) for x in row))
    conn.close()

if __name__ == "__main__":
    run(sys.argv[1])
