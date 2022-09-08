'''
1. Escriba un algoritmo que lea un número entero y determine si es par o impar. Si es par,
que escriba todos los pares de manera descendiente desde sí mismo y hasta el cero. Si
es impar, que escriba todos los impares de manera descendiente desde si sí mismo
hasta el uno. Utilice la instrucción LEER NUMERO al inicio del programa para cargar un
número en la variable NUMERO.
'''

def even_or_odd(x):
    
    myList = [x] 
    if x%2 == 0:
       for i in range(0,x):
        if i%2 == 0:
            myList.append(i)

    else:
        for i in range(1,x):
            if i%2 != 0:
                myList.append(i)

    myList.sort(reverse=True)      
    return(myList)

'''
2. Escriba un algoritmo que visualice una clasificación de 50 personas según edad y sexo.
Deberá mostrar los siguientes resultados:
a. Cantidad de personas mayores de edad (18 años o más).
b. Cantidad de personas menores de edad.
c. Cantidad de personas masculinas mayores de edad.
d. Cantidad de personas femeninas menores de edad.
e. Porcentaje que representan las personas mayores de edad respecto al total de
personas.
f. Porcentaje que representan las mujeres respecto al total de personas.
Utilice la instrucción LEER PERSONAS al inicio del programa para cargar los datos de las
50 personas en un variable, PERSONAS, que actúa como un vector de 50 posiciones.
Cada elemento de PERSONAS es de un tipo estructurado que dispone dos campos:
SEXO y EDAD.
'''

def top50 (myList):

    mas18 = 0
    menos18 = 0
    hombres_mas18 = 0
    mujeres_menos18 = 0
    pcmas18 = 0
    mujeres = 0
    pcmujeres= 0

    for i in myList:
        
        if i['sexo'] == 'femenino':
            mujeres +=1
            if i['edad']<18:
                mujeres_menos18 +=1
                menos18 +=1
            else:
                mas18 +=1
        else:
            if i['edad']<18:
                menos18 +=1
            else:
                mas18 +=1
                hombres_mas18 +=1
    
    pcmas18= mas18/int(len(myList))*100
    pcmujeres= mujeres/int(len(myList))*100
    return(mas18,menos18,hombres_mas18,mujeres_menos18,pcmas18,pcmujeres)


'''
3. Desarrolle un algoritmo para el cálculo del salario de un trabajador. El importe
liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un
condicionante sobre las horas trabajadas: si la cantidad de horas trabajadas es mayor a
40 horas, la tarifa se incrementa en un 50% para las horas extras. Calcular el sueldo
recibido por el trabajador en base las horas trabajadas y la tarifa. Utilice las
instrucciones LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para
cargar los valores en las variables HORASTRABAJADAS y TARIFA.
'''

def salary(tarifa,horas):
    if horas>40:
        extra=horas-40
        salario = tarifa*(40 + 1.5*extra)
    else:
        salario= tarifa*horas
    return salario

