from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

sonnyangels = [
    {"series": "vegetable series", "sonnyangelname": "corn", "img": "https://www.sonnyangel.com/renewal/wp-content/uploads/2019/10/Corn.png"},
    {"series":"fruit series", "sonnyangelname": "strawberry", "img": "https://www.sonnyangel.com/renewal/wp-content/uploads/2019/08/Strawberry.png"}
]

def home(request):
    return render(request, 'sonnyangel/home.html')

def about(request):
    return render(request, "sonnyangel/about.html")

def sonnyangel_index(request):
    return render(request, 'sonnyangel/index.html', {
        "sonnyangels" : sonnyangels
    })