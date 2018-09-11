#Desarrolle una aplicacion en python que pregunte al usuario
#por dos rectas, ingresando la pendiente y la interseccion con
#el eje y para cada una. Si las rectas son paralelas, el
#programa se lo informa al usuario. Si no lo son, tambien
#se lo informa y adicionalmente le muestra el punto en
#donde se intersectan.

#Recuerde que, dadas dos rectas y=m1*x+b1 e y=m2*x+b2, son paralelas
#si tienen la misma pendiente, y que el punto de interesccion entre
#ambas solo existe si no son paralelas y viene dado por:

#x=(b1-b2)/(m2-m1)

#y=(m2*b1-m1*b2)/(m2-m1)


m1 = float(raw_input("Ingrese pendiente de recta 1:"))
b1 = float(raw_input("Ingrese interseccion con el eje y de la recta 1:"))
m2 = float(raw_input("Ingrese pendiente de recta 2:"))
b2 = float(raw_input("Ingrese interseccion con el eje y de la recta 2:"))

if m1 == m2:
    print "Son paralelas!"
else:
    print "No son paralelas!"
    x = (b1 - b2) / (m2 - m1)
    y = (m2 * b1 - m1 * b2) / (m2 - m1)
    print "Se intersectan en el punto x:",x,"y:",y