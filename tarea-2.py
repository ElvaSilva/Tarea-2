print("Hola, a continuación se le va a pedir una serie de cantidades para determinar el volumen de la arepa a realizar.")
agua_tza=0
harina_tza=0
sal_cdta=0
aceite_cda=0

decision=int(input("Presione 1 si desea utilizar sus propias medidas o 2 si desea usar las medidas de Empresas Polar: 1 tza de agua y harina pan, 1 cdta de sal y 1 cda de aceite. "))
if decision == 1:
    agua_tza=float(input ("Por favor ingrese la cantidad de tazas de agua a usar "))
    harina_tza=float(input("Por favor ingrese la cantidad de tazas de harina pan "))
    sal_cdta=float(input("Por favor ingrese la cantidad de cucharaditas de sal "))
    aceite_cda=float(input("Por favor ingrese la cantidad de cucharadas de aceite "))
else:
    if decision == 2:
        agua_tza=1
        harina_tza=1
        sal_cdta=1
        aceite_cda=1
    else:
         print("Su selección no corresponde a una opción válida.")

agua_cdta=agua_tza*48
harina_cdta=harina_tza*48
aceite_cdta=aceite_cda*3
volumen_f_cdta=(agua_cdta+harina_cdta+aceite_cdta+sal_cdta)*0.9
volumen_f_cda=(volumen_f_cdta/3)
volumen_f_tza=(volumen_f_cdta/48)

decision_1=int(input("Por favor seleccione la unidad en la que quiere visualizar el volumen de la arepa: 1 para cucharaditas (cdtas), 2 para cucharadas (cdas) y 3 para tazas (tzas). "))
if decision_1 == 1:
    print("El volumen de la arepa tras la cocción es " + str(volumen_f_cdta) + " cucharaditas. Gracias por usar el programa.")
else:
    if decision_1 == 2:
        print("El volumen de la arepa tras la cocción es " + str(volumen_f_cda) + " cucharadas. Gracias por usar el programa.")
    else:
        if decision_1 == 3:
            print("El volumen de la arepa tras la cocción es " + str(volumen_f_tza) + " tazas. Gracias por usar el programa.")
        else: 
            print("Su selección no corresponde a una opción válida.")