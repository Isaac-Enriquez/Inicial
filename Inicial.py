#A00829207 Isaac Alejandro Enriquez Trejo
#A00827133 Andrea Fernanda Molina Blandon

#Este programa calcula el área
#y perímetro de un rectángulo.
def calcular_perimetro(lado1, lado2):
    perimetro = 2*lado1 + 2*lado2
    return perimetro
#funcion1  calcular área del rectángulo
def calcular_area(lado1, lado2):
    area = lado1*lado2
    return area
#funcion2  calcular perímetro del rectángulo


#instrucciones de accion
#pedir datos
print("medida de lado 1 del rectángulo")
l1 = float(input())

print("medida de lado 2 del rectángulo")
l2 = float(input())

#desplegar calculo funcion1
print(calcular_area(l1, l2))
#desplegar calculo funcion 2
print(calcular_perimetro(l1,l2))
