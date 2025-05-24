from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_CFG = {
    "dbname": os.environ.get("POSTGRES_DB", "visitasdb"),
    "user": os.environ.get("POSTGRES_USER", "guto"),
    "password": os.environ.get("POSTGRES_PASSWORD", "senha123"),
    "host": os.environ.get("DB_HOST", "db"),
    "port": 5432,
}

def get_conn():
    return psycopg2.connect(**DB_CFG)

@app.route('/visitantes')
def visitantes():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS visitas (n INT);")
            cur.execute("INSERT INTO visitas VALUES (1);")
            cur.execute("SELECT COUNT(*) FROM visitas;")
            total = cur.fetchone()[0]
            conn.commit()
    return jsonify({"total_visitas": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)