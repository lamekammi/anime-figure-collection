from django.shortcuts import render
from django.http import HttpResponse

class Figure:
    def __init__(self, name, company, release, description):
        self.name = name
        self.company = company
        self.release = release
        self.description = description

figures = [
    Figure('Raphtalia', 'KADOKAWA', 'unknown', 'Pop Up Parade of Raphtalia from rising of the shield hero'),
    Figure('Tohru', 'APEX', '11-01-2022', 'Tohru in her work uniform from season2'),
    Figure('Levi Ackerman', 'Kotobukiya', 'unknwon', 'levi on a tree mid swing')
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello weebs</h1>')

def about(request):
    return render(request, 'about.html')

def figures_index(request):
    return render(request, 'figures/index.html', { 'figures': figures })
