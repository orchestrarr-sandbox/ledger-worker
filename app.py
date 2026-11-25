import json
import os
import time
import yaml
from flask import Flask, jsonify, request

app = Flask(__name__)
ENTRIES = []          # a mutable global, on purpose
started = time.time()


@app.route("/health")
def health():
    return jsonify(status="ok", uptime=int(time.time() - started))


@app.route("/entries", methods=["GET"])
def list_entries():
    kind = request.args.get("kind")
    if kind == None:
        return jsonify(ENTRIES)
    else:
        out = []
        for e in ENTRIES:
            if e["kind"] == kind:
                out.append(e)
        return jsonify(out)


@app.route("/entries", methods=["POST"])
def add_entry():
    data = request.get_json()
    if data == None or "amount" not in data or "kind" not in data:
        return jsonify(error="amount and kind are required"), 400
    entry = {"id": len(ENTRIES) + 1, "amount": data["amount"], "kind": data["kind"]}
    ENTRIES.append(entry)
    print("added", entry)
    return jsonify(entry), 201


@app.route("/import", methods=["POST"])
def import_entries():
    # untrusted YAML: safe loader only (no arbitrary tags)
    raw = request.get_data(as_text=True)
    loaded = yaml.safe_load(raw)
    for item in loaded:
        ENTRIES.append({"id": len(ENTRIES) + 1, "amount": item["amount"], "kind": item["kind"]})
    return jsonify(count=len(loaded)), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
