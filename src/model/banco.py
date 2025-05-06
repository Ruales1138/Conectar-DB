class Banco:
    def __init__(self, codigo_banco: str, nombre_banco: str):
        self.codigo_banco: str = codigo_banco
        self.nombre_banco: str = nombre_banco
        
    def is_equal(self, otro):
        """
        Compara si la instancia actual es igual en todos sus atributos  a
        otra instancia que recibe por parametro
        """
        assert(self.codigo_banco == otro.codigo_banco, 'Los codigos de banco no coinciden')
        assert(self.nombre_banco == otro.nombre_banco, 'Los nombres de banco no coiniden')
        return True