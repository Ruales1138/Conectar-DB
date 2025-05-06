import sys
sys.path.append('src')
from model.banco import Banco
import psycopg2
import SecretConfig


class BancoController:
    def ObtenerCursor():
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        return cursor
        
    
    def insertar(banco: Banco):
        cursor = BancoController.ObtenerCursor()
        consulta = f"""
                    insert into bancos
                    (codigo_banco, nombre_banco)
                    values ('{banco.codigo_banco}', '{banco.nombre_banco}');
                    """
        cursor.execute(consulta)
        cursor.connection.commit()
    
    def buscar(codigo_banco: str):
        cursor = BancoController.ObtenerCursor()
        consulta = f"""
                    select codigo_banco, nombre_banco
                    from bancos
                    where codigo_banco = '{codigo_banco}'
                    """
        cursor.execute(consulta)
        fila = cursor.fetchone()
        resultado = Banco(codigo_banco=fila[0], nombre_banco=fila[1])
        return resultado