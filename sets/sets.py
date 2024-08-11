""" Los diccionarios son un tipo de estructura de datos que permite almacenar información. A diferencia de las listas y las tuplas, los diccionarios almacenan la información en pares de datos llamados llave y valor, donde cada valor es un elemento que corresponde a una llave. En otros lenguajes de programación, los diccionarios son conocidos como HashMaps o JSON."""

set1={1,2,3}
print(set1)

# set1[0] estop no va a funcionar

set2={1,2,3,4,5,3,3,2}
print(set2)#no se repiten se grabo en una sola 

set3={1,2.0,"hola mundoo"}
print(set3)



set1.add(34)#para agregar un solo valor
set1.update([5,6,7,8])#para agregar mas valores, OJO se debe colocar entre corchetes

print(set1)

print(len(set1))#para saber la cantidad de elementos que tiene un set
set1.discard(3)#para eliminar un elemento
print(set1)

set1.remove(5)
print(set1)

set1.clear()#elimina los elementos del set en su totalidad
