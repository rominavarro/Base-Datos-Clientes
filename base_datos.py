import sqlite3
from datetime import datetime

# Función para conectar a la base de datos
def conectar_bd():
    conexion = sqlite3.connect('droomi_store_clientes.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_cliente TEXT,
            nombre TEXT,
            telefono TEXT,
            num_orden TEXT,
            articulos TEXT,
            fecha_pedido TEXT
        )
    ''')
    conexion.commit()
    return conexion, cursor

# Función para añadir un cliente
def agregar_cliente(num_cliente, nombre, telefono, num_orden, articulos):
    conexion, cursor = conectar_bd()
    fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO clientes (num_cliente, nombre, telefono, num_orden, articulos, fecha_pedido)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (num_cliente, nombre, telefono, num_orden, articulos, fecha_pedido))
    conexion.commit()
    conexion.close()

# Función para eliminar un cliente por su número de cliente
def eliminar_cliente(num_cliente):
    conexion, cursor = conectar_bd()
    cursor.execute('''
        DELETE FROM clientes WHERE num_cliente=?
    ''', (num_cliente,))
    conexion.commit()
    conexion.close()

# Función para modificar los datos de un cliente
def modificar_cliente(num_cliente, nombre=None, telefono=None, num_orden=None, articulos=None):
    conexion, cursor = conectar_bd()
    actualizaciones = []
    if nombre:
        actualizaciones.append(('nombre', nombre))
    if telefono:
        actualizaciones.append(('telefono', telefono))
    if num_orden:
        actualizaciones.append(('num_orden', num_orden))
    if articulos:
        actualizaciones.append(('articulos', articulos))
    if actualizaciones:
        for campo, valor in actualizaciones:
            cursor.execute('''
                UPDATE clientes SET {}=? WHERE num_cliente=?
            '''.format(campo), (valor, num_cliente))
        conexion.commit()
    conexion.close()

# Función para visualizar los pedidos realizados en una fecha específica
def visualizar_pedidos_por_fecha(fecha):
    conexion, cursor = conectar_bd()
    cursor.execute('''
        SELECT * FROM clientes WHERE fecha_pedido=?
    ''', (fecha,))
    pedidos = cursor.fetchall()
    conexion.close()
    return pedidos

