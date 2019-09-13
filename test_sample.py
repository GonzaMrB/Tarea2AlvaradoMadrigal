#primera prueba, entradas correctas
from funcion import funcion
def test_funcion1():
    a=12
    b=10
    x,y,z=funcion(a,b)
    assert x==a-b
    assert y==a+b
    assert z==a*b
    
#segunda prueba, error por A<B
def test_funcion2():
    a=12
    b=13
    x=funcion(a,b)
    assert x==-1
#tercera prueba, error por valor literal
def test_funcion3():
    a=12
    b="hola"
    x=funcion(a,b)
    assert x==-1