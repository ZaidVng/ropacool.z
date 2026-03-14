from flask import Flask, request, jsonify

app = Flask(__name__)

inventario = []

@app.route("/")
def home():
    return "Sistema de inventario de Zaid funcionando"

@app.route("/agregar", methods=["POST"])
def agregar():
    data = request.json
    inventario.append(data)
    return jsonify({"mensaje": "prenda agregada", "inventario": inventario})

@app.route("/inventario")
def ver():
    return jsonify(inventario)

if __name__ == "__main__":
    app.run()