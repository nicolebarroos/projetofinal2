from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)#CharField campo de varchar
    last_name = models.CharField(max_length=30)
    age = models.IntegerField() #IntegerField é um campo inteiro
    salary = models.DecimalField(max_digits=5, decimal_places=2) #DecimalField para campos decimais///ox
    #primeiro parametro: casas antes da vírgula; segundo paramentro: casas depois da virgula
    bio = models.TextField() #TextField campo de texto
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True) #ImageField para imagens; esse parametro é opicional, sua função é
    #salvar as fotos

    def __str__(self): #O Django usará o resultado da função acima para exibir objetos desse tipo, por exemplo, na interface administrativa (admin) 
        return self.first_name + ' ' + self.last_name