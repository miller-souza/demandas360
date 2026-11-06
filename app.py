from flask import Flask, jsonify, render_template, request
from pathlib import Path
import json
from datetime import datetime, timezone

app = Flask(__name__)
DATA_FILE = Path(__file__).parent / "data" / "demandas.json"

def load_data():
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/demandas")
def demandas():
    items = load_data()
    area = request.args.get("area", "").strip().lower()
    status = request.args.get("status", "").strip().lower()
    q = request.args.get("q", "").strip().lower()
    if area:
        items = [x for x in items if x["area"].lower() == area]
    if status:
        items = [x for x in items if x["status"].lower() == status]
    if q:
        items = [x for x in items if q in x["titulo"].lower() or q in x["id"].lower()]
    return jsonify(items)

@app.get("/api/resumo")
def resumo():
    items = load_data()
    statuses = ["Em andamento", "Aguardando priorização", "Concluído"]
    return jsonify({
        "total": len(items),
        "por_status": {s: sum(1 for x in items if x["status"] == s) for s in statuses},
        "atualizado_em": datetime.now(timezone.utc).isoformat()
    })

@app.get("/api/areas")
def areas():
    return jsonify(sorted({x["area"] for x in load_data()}))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
