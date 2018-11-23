from random import randint

equipos =["F.C.Barcelona", "Real Madrid C.F.", "F.C. Bayern Munchen", "Manchester United F.C.","Juventus F.C.","Chelsea F.C.","Club Atletico de Madrid","Paris Saint-Germain F.C.","Borussia Dortmund","Manchester City F.C.","A.C. Milan","Arsenal F.C.","Liverpool F.C.","F.C. Inter de Milan","Valencia C.F.","S.S.C. Napoles","Tottenham Hotspur F.C.","A.S. Roma","F.C. Oporto","S.L. Benfica","Athletic Club","R.C.Deportivo de La Corunia","Schalke 04","Olympique de Lyon","Olympique de Marsella","S.C. Portugal","F.C. Zenit de San Petersburgo","FC Shakhtar Donetsk","Cadiz C.F.","CSKA Moscu","S.C. Braga","Montpellier HSC","FC.. Anzhi Majachkala","F.C. Rubin Kazan","Lille OSC","Abuelos F.C","Limon F.C","Huachipato","Llanfairpwllgwyngyll FC","Robin Hood","Independiente Bigote","Carabobo","Sacachispas","Semen Padang"]

contador_jornada =1

#existe una lista de los enfrentamientos ya disputados donde no pueden disputarse mas de 1 vez por temporada
#def enfrentamientos(self):  
lista_partidos_totales =[]
#cada jornada tiene 14 partidos (n-1)
jornada =contador_jornada
#existen equipos locales y visitantes 
for i in range(len(equipos)-1):
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
                if str(equipos[ran1]) != str(equipos[ran2]):
                    lista_partidos.append(partido)
                    print ('No juegan entre ellos, asi que agregamos exitosamente')
                else:
                    print ('No pueden jugar entre si')
            else:
                print ("El partido ya se jugo en esta jornada ")
        else:
            print ('El partido ya se jugo en otra fecha aparentemente')
    
    print ("Jornada-> " + str(contador_jornada))
    print ("Lista partidos:")
    for j in range(len(lista_partidos)):
        print '[' + lista_partidos[j] + ']'
    #print (lista_partidos)
    
    contador_jornada+=1


print ('###########################################')
print ('###########################################')
print ("#############-FIN EXITOSO-#################")
print ('###########################################')
print ('###########################################')