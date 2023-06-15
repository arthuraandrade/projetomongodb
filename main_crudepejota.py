from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
# pip install flask
#pip install pymongo
app= Flask(__name__)

client = MongoClient ("localhost", 27017)
db = client ['empresas_do_brasil']
collection = db["empresas"]

@app.route('/', methods= ['GET'])
def index ():
    return render_template("index.html")

@app.route ("/add", methods=['GET', 'POST'])
def add_empresa():
    if request.method == "GET":
        return render_template("addempresa.html")
    else:
        cnpj = request.form['cnpj']
        nome_fantasia = request.form['nome_fantasia']
        new_empresa= {
            'cnpj': cnpj,
            'nome_fantasia': nome_fantasia

        }
        collection.insert_one(new_empresa)
    return render_template("cadastrado_sucess.html")

if __name__ == "__main__":
    app.run()