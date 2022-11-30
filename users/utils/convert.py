from users.models import User
from rest_framework.views import Request
from datetime import datetime


def convert_file_in_string(request: Request, user: User) -> None:
    uploaded_file = request.FILES['file']

    for line in uploaded_file:
        str_user = line.decode()     
        type_valid = switch(str_user[0])
        data = {
            "type":type_valid,
            "date":datetime.strptime(str_user[1:9],"%Y%m%d").date(),
            "value":str_user[10:19],
            "cpf":str_user[19:30],
            "card":str_user[31:42],
            "hour":datetime.strptime(str_user[42:48],"%H%M%S").time(),
            "owner":str_user[48:62].rstrip(),
            "establishment":str_user[62:80].rstrip()
        }

        instance = user.objects.create(**data)
        instance.save()


def switch(compare):
    options = {
        '1': "Débito",
        '2': "Boleto",
        '3': "Financiamento",
        '4': "Crédito",
        '5': "Recebimento Empréstimo",
        '6': "Vendas",
        '7': "Recebimento TED",
        '8': "Recebimento DOC",
        '9': "Aluguel",
    }
    return options.get(compare, 'Option invalid')
