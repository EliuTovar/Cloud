from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

factores_emision = {
    'auto': 0.21,
    'avion': 0.25,
    'autobus': 0.10,
    'moto': 0.12
}

@app.route('/', methods=['GET', 'POST'])
def index():
    huella = None
    if request.method == 'POST':
        km = float(request.form['kilometros'])
        transporte = request.form['transporte']
        factor = factores_emision.get(transporte, 0)
        huella = round(km * factor, 2)
        session['ultimo_resultado'] = f'{huella} kg de CO₂ ({transporte})'
    return render_template('index.html', huella=huella)

    recomendaciones = {
    'auto': 'Considera compartir el auto o usar transporte público.',
    'avion': 'Evita vuelos cortos, usa trenes si es posible.',
    'autobus': '¡Buena elección! Es de los transportes más eficientes.',
    'moto': 'Úsala con moderación y considera caminar o usar bici.'
}



