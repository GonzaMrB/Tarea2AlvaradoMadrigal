# funcion chequea si es numero
def esnumero(x):
    try:
        float(repr(x))
        esnum = True
    except Exception:
        esnum = False
    return esnum


# funcion pedida en la tarea
def funcion(A, B):
    if(not esnumero(A) or not esnumero(B)):
        return -1
    elif(A < B):
        return -1
    else:
        X = A - B
        Y = A + B
        Z = A * B
        return X, Y, Z
