from flask import Flask, request, jsonify, render_template

app = Flask(__name__) 

from productos import productos

@app.route('/prueba',methods=['GET'])
def probarEndpoint():
    return render_template('prueba.html')

@app.route('/productos', methods=['POST'])
def addProductos():
    new_producto = {
    "name": request.json['name'],
    "price": request.json['price'],
    "quantity": request.json['quantity']
    }
    productos.append(new_producto)
    return jsonify ({"message": "los productos han sido añadidos satisfactoriamente", "productos": productos})
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)