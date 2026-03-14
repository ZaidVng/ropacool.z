from flask import Flask, request, jsonify

app = Flask(__name__)

inventario = []

@app.route("/")
def home():
    return "Sistema de inventario de Zaid funcionando"

@app.route("/agregar", methods=["POST"])
def agregar():
    data = request.form.to_dict()
    inventario.append(data)
    return jsonify(inventario)

@app.route("/inventario")
def ver():
    return jsonify(inventario)

@app.route("/form")
def form():
    return '''
    <h2>Agregar prenda</h2>
    <form action="/agregar" method="post">
        Marca:<br>
        <input name="marca"><br><br>
        Talla:<br>
        <input name="talla"><br><br>
        Precio:<br>
        <input name="precio"><br><br>
        <button type="submit">Agregar</button>
    </form>
    '''

if __name__ == "__main__":
    app.run()