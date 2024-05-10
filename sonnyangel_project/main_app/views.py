from django.shortcuts import render
from django.http import HttpResponse
from .models import Sonnyangel  , Accessories
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView



from .forms import *

# Create your views here.

# sonnyangels = [
#     {"series": "vegetable series", "sonnyangelname": "corn", "img": "https://www.sonnyangel.com/renewal/wp-content/uploads/2019/10/Corn.png", "description": "wef"},
#     {"series":"fruit series", "sonnyangelname": "strawberry", "img": "https://www.sonnyangel.com/renewal/wp-content/uploads/2019/08/Strawberry.png", "description": "efwe"}
# ]

def home(request):
    return render(request, 'sonnyangel/home.html')

def about(request):
    return render(request, "sonnyangel/about.html")

def sonnyangel_index(request):
    sonnyangels = Sonnyangel.objects.all()
    return render(request, 'sonnyangel/index.html', {
        "sonnyangels" : sonnyangels
    })

def sonnyangel_detail(request, sonnyangel_id):
    sonnyangel = Sonnyangel.objects.get(id=sonnyangel_id)
    accessories = Accessories
    id_list = sonnyangel.accessories.all().values_list('id')

    accessories_sonnyangel_doesnt_have = Accessories.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'sonnyangel/detail.html', {
    'sonnyangel': sonnyangel, 'feeding_form': feeding_form,
    'accessories': accessories_sonnyangel_doesnt_have
})

def add_sonnyangel_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.sonnyangel_id = pk
    new_feeding.save()
  return redirect('detail', sonnyangel_id=pk)

def assoc_accessories(request, pk, accessories_pk):
    Sonnyangel.objects.get(id=pk).accessories.add(accessories_pk)
    return redirect('detail', sonnyangel_id=pk)


class SonnyangelCreate(CreateView):
    model = Sonnyangel
    fields = ['name', 'breed', 'description','age']

class SonnyangelUpdate(UpdateView):
    model = Sonnyangel
    fields = ['series','sonnyangelname','description','img']

class SonnyangelDelete(DeleteView):
    model = Sonnyangel
    success_url = '/sonnyangel'



class AccessoriesList(ListView):
    model = Accessories

class AccessoriesDetail(DetailView):
    model = Accessories

class AccessoriesCreate(CreateView):
    model = Accessories
    fields = '__all__'

class AccessoriesUpdate(UpdateView):
    model = Accessories
    fields = ['name', 'color', 'description']

class AccessoriesDelete(DeleteView):
    model = Accessories
    success_url = '/accessories'