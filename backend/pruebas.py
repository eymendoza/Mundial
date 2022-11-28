from __future__ import division


precio_normal = 300 

print("mete un numero")
pan = int(input())

if pan <=6:
    multiplicacion = precio_normal * pan
    print("Seis o menos panes no tienen descuento, pagas: ", multiplicacion)

elif pan >6:
    operacion = precio_normal * pan 
    resta = operacion - (operacion * 0.6)
    print("Precio normal: ",operacion)
    print("Te descontamos: ",operacion*0.6)
    print("Tienes que pagar: ", resta)