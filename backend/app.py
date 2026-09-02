from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "database"),
        database=os.getenv("DB_NAME", "rrhh"),
        user=os.getenv("DB_USER", "rrhh_user"),
        password=os.getenv("DB_PASSWORD", "rrhh_pass")
    )


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API de Recursos Humanos - Inti Punku",
        "estado": "funcionando"
    })


@app.route("/api/departamentos")
def departamentos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_departamento, nombre, descripcion
        FROM departamentos
        ORDER BY id_departamento
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    resultado = []

    for fila in datos:
        resultado.append({
            "id": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2]
        })

    return jsonify(resultado)


@app.route("/api/cargos")
def cargos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_cargo, nombre, descripcion
        FROM cargos
        ORDER BY id_cargo
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    resultado = []

    for fila in datos:
        resultado.append({
            "id": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2]
        })

    return jsonify(resultado)


@app.route("/api/empleados")
def empleados():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            e.id_empleado,
            e.nombre,
            e.apellido,
            e.email,
            e.telefono,
            e.fecha_ingreso,
            d.nombre AS departamento,
            c.nombre AS cargo
        FROM empleados e
        JOIN departamentos d
            ON e.id_departamento = d.id_departamento
        JOIN cargos c
            ON e.id_cargo = c.id_cargo
        ORDER BY e.id_empleado
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    resultado = []

    for fila in datos:
        resultado.append({
            "id": fila[0],
            "nombre": fila[1],
            "apellido": fila[2],
            "email": fila[3],
            "telefono": fila[4],
            "fecha_ingreso": str(fila[5]),
            "departamento": fila[6],
            "cargo": fila[7]
        })

    return jsonify(resultado)


@app.route("/api/resumen")
def resumen():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM empleados")
    empleados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM departamentos")
    departamentos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cargos")
    cargos = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({
        "empleados": empleados,
        "departamentos": departamentos,
        "cargos": cargos
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)