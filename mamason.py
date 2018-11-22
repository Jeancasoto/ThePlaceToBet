from random import randint

equipos = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P']

contador_jornada =1

#existe una lista de los enfrentamientos ya disputados donde no pueden disputarse mas de 1 vez por temporada
#def enfrentamientos(self):  
lista_partidos_totales =[]
#cada jornada tiene 14 partidos (n-1)
jornada =contador_jornada
#existen equipos locales y visitantes 
for i in range(len(equipos)):
    lista_partidos = []
    while len(lista_partidos) <14:
        ran1=randint(0,len(equipos)-1)
        ran2=randint(0,len(equipos)-1)
        partido = equipos[ran1]+"-"+equipos[ran2]
        if partido not in lista_partidos_totales:
            print ("No se ha jugado en otra fecha")
            lista_partidos_totales.append(partido)
            if partido not in lista_partidos:
                print ("No se ha jugado esta jornada")
                lista_partidos.append(partido)
            else:
                print ("El partido ya se jugo en esta jornada ")
        else:
            print ('El partido ya se jugo en otra fecha aparentemente')
    
    print ("Jornada-> " + str(contador_jornada))
    print ("Lista partidos:")
    #for j in len(lista_partidos):
    #    print 'Juego:'+j+" "+lista_partidos[j]
    print (lista_partidos)
    
    contador_jornada+=1