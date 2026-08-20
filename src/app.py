from flask import Flask, jsonify
import mysql.connector

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
    app.run(host="0.0.0.0", port=5000)