from django.shortcuts import render, redirect
from .models import Room, users
from .serializer import RoomSerializer
from .analizecsv import df_result
from rest_framework import generics
from django.http import HttpResponse
from .forms import UserForm

class RoomsAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def indexView(request):
    return render(request, 'myapi/index.html', {'title': "Example 2",
                                                'msg': "Hi, World!"})

def download_room_csv(request):
    df = df_result
    temp_file_path = 'temp_excel_file.xlsx'
    df.to_excel(temp_file_path, index=False, engine='openpyxl')

    with open(temp_file_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(),
                                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=rooms.xlsx'

    import os
    os.remove(temp_file_path)

    return response

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not users.objects.filter(email=email).exists():
                form.save()
                return redirect('myapi/add_user.html')  # Замените 'success_page' на ваше имя URL-шаблона
            else:
                error_message = 'Пользователь с таким email уже существует.'
    else:
        form = UserForm()
        error_message = None
    return render(request, 'myapi/add_user.html', {'form': form, 'error_message': error_message})