from rest_framework.views import Request
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from users.models import User
from .utils.convert import convert_file_in_string
import ipdb
from django.db.models import Sum


# Create your views here.
def upload_file(request: Request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            convert_file_in_string(request, User)

            return redirect('/user/list/establishments/')
    else:
        form = UploadFileForm()
    return render(request, 'users/upload.html', {'form': form})


def list_establishments(request: Request):
    if request.method == 'GET':
        users = User.objects.all()
        list_establishments = []
        establishments_valid = verify_establishment(users)

        def list_all_establishments():
            for establishment in establishments_valid:
                value = 0
                for user in users:
                    if user.establishment == establishment:
                        value += user.value
                list_establishments.append(
                    {"establishment": establishment, "value": value}
                )

            return list_establishments
        list_all_establishments()
        return render(
            request,
            "users/list.html",
            {"list_establishments": list_establishments}
        )


def verify_establishment(users):
    establishment_list = []
    for user in users:
        verify = establishment_list.count(user.establishment)
        if verify != 0:
            ...
        else:
            establishment_list.append(user.establishment)
    return establishment_list
