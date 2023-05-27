import unittest
import subprocess

class TestCalculator(unittest.TestCase):
    def test_multiplicacion(self):
        res = subprocess.check_output(['python3', 'calculadora.py', '5', '3'])
        res = res.decode().strip()
        self.assertEqual(res.strip(), "Resultado: 15.0")

if __name__ == '__main__':
    unittest.main()
