from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "mensaje": "Hola Mundo desde Flask con Docker",
        "estado": "OK"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)