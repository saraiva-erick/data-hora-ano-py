from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Obter a data e hora atual
    now = datetime.datetime.now()

    # Calcular quantos dias restam até o final do ano
    end_of_year = datetime.datetime(now.year, 12, 31)
    days_left = (end_of_year - now).days

    # Renderizar o template HTML com os dados
    return render_template('index.html',
                           weekday=now.strftime("%A"),
                           date=now.strftime("%d/%m/%Y"),
                           days_passed=now.timetuple().tm_yday,
                           days_left=days_left)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

