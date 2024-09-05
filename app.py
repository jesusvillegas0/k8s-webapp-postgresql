from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__)

# Ruta para mostrar el formulario HTML
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para procesar los datos del formulario
@app.route('/submit-data', methods=['POST'])
def submit_data():
    name = request.form['name']  # Obtiene el nombre del formulario
    conn = psycopg2.connect(
        host="postgres",
        database="mydb",
        user="user",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO mytable (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'success', 'name': name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
