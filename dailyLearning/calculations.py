from logcall import logged

@logged
def add(x, y):
    '''
    Add x and y
    '''
    return x + y

@logged
def sub(x, y):
    '''
    Subtract y from x
    '''
    return x - y

@logged
def mult(x, y):
    '''
    Multiple x and y
    '''
    return x * y


if __name__ == '__main__':
    print(add(9, 9))