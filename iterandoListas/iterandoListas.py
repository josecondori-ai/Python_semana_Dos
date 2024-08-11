"""
 En Python tenemos diferentes opciones para iterar sobre una lista, ya que podemos usar tanto el ciclo for como el ciclo while, sin embargo, la selección del tipo de ciclo depende de la necesidad de cada desarrollador. Para iterar sobre una lista usando el ciclo for podemos hacerlo de dos maneras: la primera es iterando directamente sobre la lista"""

nombres=['luis','pedro','mario']
for elemento in nombres:
    print(elemento)



    """ La segunda manera en la que podemos iterar sobre la lista es usando los índices. Para ello, necesitaremos combinar las funciones range y len. """


    for index in range(len(nombres)):
        print("indice",index)
        print("elemento",nombres[index])

        