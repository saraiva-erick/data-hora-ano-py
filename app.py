import datetime

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    # Obter a data e hora atual
    now = datetime.datetime.now()

    # Calcular quantos dias restam até o final do ano
    end_of_year = datetime.datetime(now.year, 12, 31)
    days_left = (end_of_year - now).days

    # Retornar os dados
    return ('<h1>Bem-vindo(a) ao programa de data e hora em Flask/Python!</h1>',
            '<p> Hoje é: ' + now.strftime("%A") '</p>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
