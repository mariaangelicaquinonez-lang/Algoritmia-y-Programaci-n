nombre_gato = input( "Pon el nombre de tu gato: ")
caricias = 0

def acariciar(): 
    global caricias
    caricias += 1
    print( f"{nombre_gato} fue acariciao/a {caricias} vez/veces")


for i in range(3):
    acariciar()   