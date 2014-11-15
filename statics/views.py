from django.shortcuts import render

def home(request, page="0"):
        return render(request, "home.html")
