# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from apps.pets.models import Pet, News

def about(request):
	html = "Hola que hace?"
	return HttpResponse(html)


def home(request):
    template_name='home.html'
    pets = Pet.objects.all()
    return render(request, template_name, { 'pets': pets })

def pet_detail(request, pet_id):
    """
    Return a specific pet with its info
    """
    template_name='pets/pets_detail.html'
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(
        request,
        template_name,
        {'pet': pet}
    )

class NewsDetail(DetailView):
    model = News