def fibonacci():
    a = int (input("ingrese el límite máximo de la serie fibonacci"))
    if (a<0):
        print ("el número no puede ser negativo")
        fibonacci ()
    b = 0
    c = 1
    iterm = 0
    while (iterm < a-1):
        result = b + c
        b = c
        c = result
        iterm = iterm + 1
        print (b, ' - ')
        
        
fibonacci()
