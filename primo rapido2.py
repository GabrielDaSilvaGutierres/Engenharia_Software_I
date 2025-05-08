from math import ceil, sqrt

def primo(n):
    if n % 2 == 0: return n == 2
    raiz = ceil(sqrt(n))
    for pd in range(3, raiz+1, 2):
        if n % pd == 0:
            return False
        return True

def main():
    qtd = int(input())
    for i in range(qtd):
        n = int(input())
        if primo(n):
            print('Prime')
        else:
                print('Not Prime')

main()
