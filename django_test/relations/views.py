from django.http import HttpResponse
from relations.models import Car, Car_owner, Colors

# Create your views here.

def test(request):
    
    #car_owners = Car_owner.objects.all()
    #for car_owner in car_owners:
        #print (car_owner.name) #con esto muestra el dato del nombre por consola de VS al actulizar la pagina
        #print (car_owner.owned_car.color.name)  #con esto muestra el dato del color por consola de VS al actualizar la pagina
        #con esto unimos tres tablas, el dueño tiene un auto (>models>class Car_owner y class Car); y el auto tiene un color (>models>class Car y class Colors)

    colors = Colors.objects.all()   #yo estoy agarrando todos los colores de la base de datos
    
    for color in colors:            #y por cada uno de ellos, le pregunto que auto tiene ese color
        print(color.car)            #por un lado nos dice el color
        print(color.car.all())      #nos trae una lista con todos los autos que sean de ese color >> Car: Car Object (1)



    return HttpResponse('Listo')