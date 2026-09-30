from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome To My Shop!</h1><p>Project Completed By Trupti</p>")
