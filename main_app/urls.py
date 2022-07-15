from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('figures/', views.figures_index, name='index'),
    path('figures/<int:figure_id>/', views.figures_detail, name='detail'),
    path('cats/create/', views.FigureCreate.as_view(), name="figures_create"),
]