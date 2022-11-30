from django.db import models
import uuid

# Create your models here.
class types(models.TextChoices):
    debit = "Débito"
    ticket = "Boleto"
    financing = "Financiamento"
    credit = "Crédito"
    loan = "Recebimento Empréstimo"
    sale = "Vendas"
    ted = "Recebimento TED"
    doc = "Recebimento DOC"
    rent = "Aluguel"

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=50,choices=types.choices)
    date = models.DateField()
    hour = models.TimeField()
    value = models.PositiveIntegerField()
    cpf = models.CharField(max_length=50)
    card = models.CharField(max_length=50)
    establishment = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, unique=False, )
    
