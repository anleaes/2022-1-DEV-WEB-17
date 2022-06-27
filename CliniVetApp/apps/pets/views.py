from django.shortcuts import render, get_object_or_404, redirect
from .forms import PetsForm
from .models import Pets

# Create your views here.

def add_pets(request):
    template_name = 'pets/add_pets.html'
    context = {}
    if request.method == 'POST':
        form = PetsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pets:list_pets')
    form = PetsForm()
    context['form'] = form
    return render(request, template_name, context)

def list_pets(request):
    template_name = 'pets/list_pets.html'
    pets = Pets.objects.filter()
    context = {
        'pets': pets
    }
    return render(request, template_name, context)

def edit_pets(request, id_pets):
    template_name = 'pets/add_pets.html'
    context ={}
    pets = get_object_or_404(Pets, id=id_pets)
    if request.method == 'POST':
        form = PetsForm(request.POST, instance=pets)
        if form.is_valid():
            form.save()
            return redirect('pets:list_pets')
    form = PetsForm(instance=pets)
    context['form'] = form
    return render(request, template_name, context)

def delete_pets(request, id_pets):
    pets = pets.objects.get(id=id_pets)
    pets.delete()
    return redirect('pets:list_pets')
