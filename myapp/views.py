from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from myapp.models import Room, Message


# Create your views here.
def index(request):
    return render(request, 'login.html')


def sign_up(request):
    message = 'myapp'
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Password = request.POST['Password']
        confirm_password = request.POST['confirm_password ']
        if username != '':
            if Password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist')
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already exist')
                    return redirect('sign_up')

                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=Password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, 'password not the same')
                return redirect('sign_up')
        elif username == '':
            messages.info(request, )
            return redirect('sign_up')
    else:
        return render(request, 'sign_up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']
        user = auth.authenticate(username=username, password=Password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/')


def swee(request):
    pass


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
