from flask import Flask, request, jsonify

app = Flask(__name__)

# Nueva ruta para la raíz
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the WebApp!"

@app.route('/data', methods=['POST'])
def insert_data():
    data = request.json
    conn = psycopg2.connect(
        host="postgres",
        database="mydb",
        user="user",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO mytable (name) VALUES (%s)", (data['name'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
