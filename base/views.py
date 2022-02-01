from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Python Crash Course'},
    {'id':2, 'name':'React Font to Back'},
    {'id':3, 'name':'Laravel From Scratch'},
]

def home(request):
    context= {'rooms':rooms}
    return render (request,'base/home.html',context)

def room(request,pk):

    room=None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    context = {'room':room}
    return render (request,'base/room.html',context)

