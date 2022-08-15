from pyexpat import model
from django.db import models

# Create your models here.

#creamos las clases a las que va a estar relacionado el auto. Creamos dos clases muy simples (clases complementarias)
class Car_owner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Colors(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    owner = models.OneToOneField(Car_owner, on_delete=models.CASCADE, related_name='owned_car') #suponemos que tiene un solo dueño #le decimos a que modelo estar relacionado (en este caso Car_owner), y que pasa cuando borramos uno (con on_delete). En este caso si yo borro un dueño tambien borrame los datos del auto, o si yo borro un auto borrame los datos del dueño.
    color = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True, blank=True, related_name='car') #le decimos que esta relacionado con colores con "Colors"; le decimos que pase si borro un color con "on_delete" con SET_NULL le indico que el campo es nulo / la otra opcion es CASCADE que significa borra el auto / y la otra opcion es RESTRIC que significa no dejes borrar un color si hay autos asignados.
    #ademas le tengo que aclarar que el campo puede ser nulo cuando borro un color con: null=True y blank=True
    #que pasa si a un color, le quiero pedir todos los autos que tengan ese color, tengo que unsar related_name='car'; este 'car' lo usamos para poder usarlo desde class Colors, si nosotros decimos Colors.car me va a traer dos autos de los cuales sea un color
