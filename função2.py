def maximo(a, b):
    if a > b:
        return a
    else:
        return b
    x = int(input('numero: '))
    y = int(input('numero: '))

    m = maximo(x, y)

    print('máximo: %d' % m)
        
