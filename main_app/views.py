from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Figure
from .forms import CommentForm

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
    comment_form = CommentForm()
    return render(request, 'figures/detail.html', { 
        'figure': figure,
        'comment_form': comment_form })

class FigureCreate(CreateView):
    model = Figure
    fields = '__all__'

class FigureUpdate(UpdateView):
    model = Figure
    fields = '__all__'

class FigureDelete(DeleteView):
    model = Figure
    success_url = '/figures/'

def add_comment(request, figure_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.figure_id = figure_id
        new_comment.save()
    return redirect('detail', figure_id=figure_id)