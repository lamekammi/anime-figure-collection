from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('figures/', views.figures_index, name='index'),
    path('figures/<int:figure_id>/', views.figures_detail, name='detail'),
    path('figures/create/', views.FigureCreate.as_view(), name="figures_create"),
    path('figures/<int:pk>/update/', views.FigureUpdate.as_view(), name='figures_update'),
    path('figures/<int:pk>/delete/', views.FigureDelete.as_view(), name='figures_delete'),
    path('figures/<int:figure_id>/add_comment/', views.add_comment, name='add_comment'),
    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('figures/<int:figure_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store')
]