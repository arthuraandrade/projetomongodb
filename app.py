from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
# pip install flask
#pip install pymongo
app= Flask(__name__)

client = MongoClient ("localhost", 27017)
db = client ['veiculos']
collection = db["carros"]

@app.route('/', methods= ['GET'])
def index ():
    return render_template("index.html")

@app.route ("/add", methods=['GET', 'POST'])
def add_carro():
    if request.method == "GET"
        return render_template("addcarro.html")
    else:
        Marca= request.form['marca']
        Modelo = request.form['modelo']
        Preco = request.form['preco']
        Ano = request.form['ano']
        Categoria = request.form['categoria']
        Cambio = request.form['cambio']

        carro= {
            'Marca': Marca,
            'Modelo': Modelo,
            'Preco': Preco,
            'Ano': Ano,
            'Categoria': Categoria,
            'Cambio': Cambio

        }


    new_car = {"Marca": "Ford","Modelo": "Bronco","Ano": 2023, "Preco": 140000}
    collection.insert_one(new_car)
    return render_template("sucesso.html")

if __name__ == "__main__":
    app.run()