import oracledb

def get_connection():
    try:
        connection = oracledb.connect("rm/password@host:port/orcl")
        print("connected")
    except Exception as e:
        print(f'error obtaining a connection: {e} ')
    return connection


def listar():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM t_cliente'
    cursor.execute(sql)


    for linha in cursor: 
        print(linha)

    cursor.close()
    connection.close()


def listing():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO t_cliente VALUES (2, 'Oliveira')"
    cursor.execute(sql)
    connection.commit()
    print("data inserted!")
    cursor.close()
    connection.close()


def insert_params(codigo, nome):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO t_cliente (codigo, nome) VALUES ({codigo}, {nome})"
    data = (codigo, nome)
    cursor.execute(sql, data)
    connection.commit()
    print(f'data inn')
    cursor.close()
    connection.close()



def update():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "UPDATE t_cliente SET nome = 'Julio' WHERE codigo = 2"
    cursor.execute(sql)
    connection.commit()
    print(f'data updated')
    cursor.close()
    connection.close()


def delete():
    connection =  get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM t_cliente WHERE codigo = 1"
    cursor.execute(sql)
    connection.commit()
    print(f'data deleted')
    cursor.close()
    connection.close()



connection = get_connection()
print(f'version: {connection.version}')
print()
insert()
listing()
update()
delete()
insert_params(5, 'fernando')