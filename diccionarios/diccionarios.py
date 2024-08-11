"""Los diccionarios son un tipo de estructura de datos que permite almacenar información. A diferencia de las listas y las tuplas, los diccionarios almacenan la información en pares de datos llamados llave y valor, donde cada valor es un elemento que corresponde a una llave. En otros lenguajes de programación, los diccionarios son conocidos como HashMaps o JSON."""

comida={
    "nombre":"pasta",
    "origen":"italia"
}

print(comida)

#para acceder a sua valores usamos
print(comida["nombre"])


#para agregar mas infomacion a los diccionario
comida["fecha_creacion"]=1750
print(comida)

comida["caracteristicas"]=["rapido","rico"]

print(comida)

print(comida.items())#esto nos retornara una lista de tuplas donde cada tupla es una combinacion de cada llave con sus respectivo valor
print(comida.keys())#nos retornara la lista de las llaves del diccionario
print(comida.values())#nos retornara la lista de los valores del diccionario