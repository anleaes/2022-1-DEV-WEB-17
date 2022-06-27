from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServicesForm
from .models import Services

# Create your views here.

def add_services(request):
    template_name = 'services/add_services.html'
    context = {}
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('services:list_services')
    form = ServicesForm()
    context['form'] = form
    return render(request, template_name, context)

def list_services(request):
    template_name = 'services/list_services.html'
    services = Services.objects.filter()
    context = {
        'services': services
    }
    return render(request, template_name, context)

def edit_services(request, id_services):
    template_name = 'services/add_services.html'
    context ={}
    services = get_object_or_404(Services, id=id_services)
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES,  instance=services)
        if form.is_valid():
            form.save()
            return redirect('services:list_services')
    form = ServicesForm(instance=services)
    context['form'] = form
    return render(request, template_name, context)

def delete_services(request, id_services):
    services = Services.objects.get(id=id_services)
    services.delete()
    return redirect('services:list_services')