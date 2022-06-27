from django.db import models
from django.db import models
from pets.models import Pets
# Create your models here.

class Client(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    Status_CHOICES = (
        ('V', 'Vip'),
        ('N', 'Normal'),
    )
    status = models.CharField('status', max_length=1, choices=Status_CHOICES)
    client_pets = models.ManyToManyField(Pets, through='client_pets1', blank=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name


class client_pets1(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pets = models.ForeignKey(Pets, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'pets'
        verbose_name_plural = 'pets'
        ordering =['id']

    def __str__(self):
        return self.pets.name
