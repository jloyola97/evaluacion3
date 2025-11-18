from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'super_secreto'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1.html', methods=['GET', 'POST'])
def ejercicio1():
    # Inicializa las variables de resultado como None
    promedio = None
    estado = None

    if request.method == 'POST':
        try:
            # Obtiene los datos del formulario y los convierte a float
            # El atributo 'name' en el HTML (ej: name="nota1") es la clave aquí
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Calcula el promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # Determina el estado del estudiante (ejemplo de lógica simple)
            if promedio >= 4.0 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

        except (ValueError, KeyError) as e:
            # Maneja errores si los datos no son válidos o faltan
            flash("Error en los datos ingresados: {e}", "error")

    # Renderiza la plantilla, pasando los resultados si existen
    return render_template('Ejercicio 1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return render_template('Ejercicio 2.html')

if __name__ == '__main__':
    app.run()
