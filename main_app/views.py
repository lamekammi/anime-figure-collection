from django.shortcuts import render
from django.http import HttpResponse

class Figure:
    def __init__(self, name, company, release, description):
        self.name = name
        self.company = company
        self.release = release
        self.description = description

figures = [
    Figure(),
    Figure(),
    Figure()
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello weebs</h1>')

def about(request):
    return render(request, 'about.html')

def figures_index(request):
    return render(request, 'figures/index.html', { 'figures': figures })
