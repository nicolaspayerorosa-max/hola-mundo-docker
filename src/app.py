from flask import Flask
import mysql.connector

app = Flask(__name__)

def conectar_bd():
    conexion = mysql.connector.connect(
        host="mysql",
        user="root",
        password="123456",
        database="hola_mundo"
    )
    return conexion

@app.route("/")
def inicio():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes(
                id INT AUTO_INCREMENT PRIMARY KEY,
                texto VARCHAR(100)
            )
        """)

        cursor.execute("""
            INSERT INTO mensajes(texto)
            VALUES('Hola Mundo desde Docker')
        """)

        conexion.commit()

        cursor.execute("SELECT * FROM mensajes")
        datos = cursor.fetchall()

        conexion.close()

        return f"""
        <h1>Hola Mundo con Flask y Docker</h1>
        <h2>Datos guardados en MySQL:</h2>
        {datos}
        """

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)