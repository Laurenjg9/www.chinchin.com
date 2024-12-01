from flask import Flask, render_template          # Importo la libreria de Flask


# Variable que nos permite controlar la aplicacion y desplegarla 
app = Flask(__name__)                             # Crear la aplicacion: Indica y verifica que estamos trabajando en el archivo incial del proyecto              

# Estoy indicando una ruta, definiendo la ruta raiz
@app.route("/")
# Metodo que me retorna la informacion de la ruta inicial de la pagina
def index():
    return render_template('index.html')

@app.route("/tips.html")
def tips():
    return render_template('tips.html')

@app.route("/creadores.html")
def creadores():
    return render_template('creadores.html')


# Ver en el navegador el resultado
if __name__ == "__main__":
    port=5003
    app.run(port=port,debug=True)          # Con esta instruccion estoy dando a enten Que estoy en el proceso de desarrollo, lo que hace es que el servidor se reinicia automaticamente cuando la aplicacion tenga un cambio y se guarde

