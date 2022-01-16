#Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
#Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
#Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
#Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.


fecha_kmdt=input("Fecha (formato 'día, DD/MM'): ")
fecha_kmdt=fecha_kmdt.lower()
diasemana_kmdt=fecha_kmdt[0:fecha_kmdt.find(',')]
dianro_kmdt=int(fecha_kmdt[fecha_kmdt.find(',')+2:fecha_kmdt.find('/')])
mesnro_kmdt=int(fecha_kmdt[fecha_kmdt.find('/')+1:])
if dianro_kmdt>31 or mesnro_kmdt>12:
    print("Fecha incorrecta")
else:
    if diasemana_kmdt in "lunes,martes,miércoles":
        respuesta_kmdt=input("¿Se tomaron exámenes? S/N: ")
        if respuesta_kmdt.lower()=="s":
            aprobados_kmdt=int(input("Cantidad de aprobados: "))
            reprobados_kmdt=int(input("Cantidad de reprobados: "))
            print("Porcentaje de aprobados:", (aprobados_kmdt*100)/(aprobados_kmdt+reprobados_kmdt), "%")
    elif diasemana_kmdt=="jueves":
        asistencia_kmdt=int(input("Porcentaje de asistencia: "))
        if asistencia_kmdt>50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif diasemana_kmdt=="viernes":
        if dianro_kmdt==1 and (mesnro_kmdt==1 or mesnro_kmdt==7):
            print("Nuevo ciclo")
            alumnos_kmdt=int(input("Cantidad de alumnos: "))
            arancel_kmdt=float(input("Arancel: $"))
            print("Ingreso total: $", alumnos_kmdt*arancel_kmdt)
    else:
        print("Fecha incorrecta")
print("Fin del programa")