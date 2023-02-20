from django.shortcuts import render
from django.http import HttpResponse

# Ejercicios
#1
n=50
acum=0
for i in range(n+1):
    acum=acum+i
def sumaCincuentanumeros(request,*cadena,**cadenaI):
    return render(request,"ejercicio1.html",{'suma':acum})

#2
num=7
f=1
for i in range(1,num+1):
    f*=i
def factorialdeunnumero(request,*cadena,**cadenaI):
    return render(request,"ejercicio2.html",{'factorial':f})

#3
so=['windows','linux','mac']
for sistema in so:
	print(sistema)          
def listadesistemas(request,*cadena,**cadenaI):
    return render(request,"ejercicio3.html",{'sistemas':so})

#4
frase="Tres tristes tigres tragaban trigo de un trigal"
letra="e"
contador = 0
for i in frase:
    if i == letra:
        contador += 1
p=["La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase)]
def letrayfrase(request,*cadena,**cadenaI):
    return render(request,"ejercicio4.html",{'apariciones':p})

#5
edades = [18,23,30,35,39,42,63]
cantidad =0
for num in edades:
	if (num%3 == 0):
		cantidad+=1
g=[cantidad]
def multiplodetres(request,*cadena,**cadenaI):
    return render(request,"ejercicio5.html",{'cantidadmultiplo':g})

#6
i=1
sumar=0
while i<=25:
    sumar += i 
    i += 1 
    print(sumar)
def numeroshastaveinte(request,*cadena,**cadenaI):
    return render(request,"ejercicio6.html",{'hastaveinticinco':sumar})

#7
suma=0
cont=0
num=1
while num<=10:
    suma+=num
    cont+=1
    num+=1
    prom=suma/cont
    print(prom)
def promedionumeros(request,*cadena,**cadenaI):
    return render(request,"ejercicio7.html",{'promedio':prom})

#8
cont=0
suma=0 
while cont<100:
    suma=suma+cont
    cont+=4
    print(suma)
def sumamutiplocuatro(request,*cadena,**cadenaI):
    return render(request,"ejercicio8.html",{'sumamultiplo':suma})

#9
numini=5
numfin=15
cant=0
while numini<numfin:
    if numini % 2 == 0: 
        print(numini)
        cant+=1
    numini+=1 
print(cantidad)
def cantidadpar(request,*cadena,**cadenaI):
    return render(request,"ejercicio9.html",{'pares':cantidad})

#10
n=11
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)
def sumaenterosposi(request,*cadena,**cadenaI):
    return render(request,"ejercicio10.html",{'cantidadfinal':sum})

#11
numeroveinte=[]
i=0
while True:
    i=i+1
    if i>20:
        break
    numeroveinte.append(i)
def numerosenterosveinte(request,*cadena,**cadenaI):
    return render(request,"ejercicio11.html",{'veinte':numeroveinte})
     
#12
veinticinco=[]
i=26
while True:
    i=i-1
    if i<0:
        break
    veinticinco.append(i)
def numerosdesdeveinticinco(request,*cadena,**cadenaI):
    return render(request,"ejercicio12.html",{'descendentes':veinticinco})

#13
mulcinco=[]
i=0
while True:
    i=i+5
    if i>50:
        break
    mulcinco.append(i)
def multiplosdecinco(request,*cadena,**cadenaI):
    return render(request,"ejercicio13.html",{'multiplosdelcinco':mulcinco})

#14
suma=0
cont=0
num=1
while True:
    promedio=float()
    suma+=num
    cont+=1
    num+=1
    promedio=suma/cont
    if num==51:
        break
    print(promedio)
def promediocincuentanumeros(request,*cadena,**cadenaI):
    return render(request,"ejercicio14.html",{'promediocincuenta':promedio})

#15
impares=[]
i=0
while True:
    i=i+3
    if i>60:
        break
    impares.append(i)
def imparalsesenta(request,*cadena,**cadenaI):
    return render(request,"ejercicio15.html",{'imparess':impares})
     