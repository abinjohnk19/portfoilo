from django.shortcuts import render
from .models import Contact

def home(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )

    return render(request, "home/index.html")
