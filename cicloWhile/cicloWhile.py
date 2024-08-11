""" El ciclo while ejecuta una o más instrucciones mientras se cumple una condición. Normalmente, en el ciclo while usamos un contador que nos permite saber hasta cuándo debemos repetir el ciclo. Esta vez vamos a definir el contador como «i = 1», es decir, nuestro contador va a empezar en el número 1. Luego, definimos la instrucción para el ciclo «while» y la condición sobre la cual el ciclo va a iterar. En este caso, será que el contador sea «<= 5». Escribimos dos puntos para indicar que las líneas indentadas siguientes pertenecerán al bloque while. En el bloque while vamos a imprimir el valor del contador y después incrementaremos el valor del contador en 1"""


# i=0
# while i<=5:
#     print(i)
#     i+=1


i=1
while i<=5:

    print(i)
    i+=1
    if i==3:
        break




    #podemos usar el break y el continue para romper el ciclo