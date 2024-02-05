from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Menu
# Create your views here.


def index(request):
    title = "Raniel's Restaurant"
    return render(request, 'index.html', {'title': title})

def about(request):
    title =  "About Us"
    return render(request, 'about.html', {'title': title})

def contact(request):
    title = "Contact Raniel's Restaurant"
    return render(request, 'contact.html', {'title':title})


# Add your code here to create new views
#Menu Function

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    title =  "Book a Table Now!"
    return render(request,'book.html',{'title':title, **context})
    

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data, })


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})

