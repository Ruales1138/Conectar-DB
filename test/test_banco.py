import unittest
import sys
sys.path.append('src')
sys.path.append( "." )
from model.banco import Banco
from controller.banco_controller import BancoController


class TestTarjeta( unittest.TestCase ):
    def test_insertar(self):
        banco = Banco(codigo_banco = '07', nombre_banco = 'Bancolombia')
        BancoController.insertar(banco)
        banco_buscado = BancoController.buscar('07')
        self.assertTrue(banco_buscado.is_equal(banco))
        
        
if __name__ == '__main__':
    unittest.main()