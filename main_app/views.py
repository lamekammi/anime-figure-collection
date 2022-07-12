from django.shortcuts import render
from .models import Figure

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def figures_index(request):
    figures = Figure.objects.all()
    return render(request, 'figures/index.html', { 'figures': figures })

def figures_detail(request, figure_id):
    figure = Figure.objects.get(id=figure_id)
    return render(request, 'figures/detail.html', { 'figure': figure })

