lines (7 sloc)  217 Bytes
   
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])

def say_hello():
    return jsonify({"text": "Semangat Saipullah"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)