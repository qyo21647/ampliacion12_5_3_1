import unittest
import subprocess

class test_calculator(unittest.TestCase):
    def test_multiplicacion(self):
        res = subprocess.check_output(['python3', 'calculadora.py', '5', '3'])
        res = res.decode().strip()
        self.assertEqual(res, "Resultado: 15")

if __name__ == '__main__':
    unittest.main()
