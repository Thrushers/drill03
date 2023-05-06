###Lista completa de los nombres###

def imprimir_nombres(*nombres):
    return nombres[0]
    

nombres = ["Harry Houdini","Newton","David Blaine","Hawking","messi","teller","einstein","pele","juanes" ]
print(imprimir_nombres(nombres))

###Lista de los magos###

def imprimir_magos():
    nombres = ["Harry Houdini","Newton","David Blaine","Hawking","messi","teller","einstein","pele","juanes" ]
    magos = [nombres[0],nombres[2],nombres[5]]
    print(magos)


magos = [nombres[0],nombres[2],nombres[5]]

def hacer_grandioso(*magos):
    
    magos2 = ["El grandioso "+ magos[0][0],"El grandioso "+ magos[0][1],"El grandioso "+ magos[0][2]]
    return magos2
hacer_grandioso(magos)


###Lista de los cientificos###

def imprimir_cientifico():
    nombres = ["Harry Houdini","Newton","David Blaine","Hawking","messi","teller","einstein","pele","juanes" ]
    cientifico = [nombres[1],nombres[3],nombres[6]]
    print(cientifico)


###Lista de otros###
def imprimir_otros():
    nombres = ["Harry Houdini","Newton","David Blaine","Hawking","messi","teller","einstein","pele","juanes" ]
    magos = [nombres[0],nombres[2],nombres[5]]
    cientifico = [nombres[1],nombres[3],nombres[6]]
    
    for i in magos:
        nombres.remove(i)

    for i in cientifico:
        nombres.remove(i)
    print(nombres)
  

def imprimir_todos():
    imprimir_magos()
    imprimir_cientifico()
    imprimir_otros()
imprimir_todos()

print(hacer_grandioso(magos))
