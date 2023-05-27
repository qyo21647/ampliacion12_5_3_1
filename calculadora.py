import sys

def multiplicar(multiplicando, multiplicador):

    return multiplicando * multiplicador

if __name__ == '__main__':
       multi1 = float(sys.argv[1])
       multi2 = float(sys.argv[2])
       res = multiplicar(multi1, multi2)
       print("Resultado:",res)
