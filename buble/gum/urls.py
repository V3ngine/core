from django import views
from django.urls import path

from . import views

app_name = 'gum'

urlpatterns = [
    path('index', views.index, name='index'),
    path('regform', views.regform, name='regform'),
    path('base', views.base, name='base'),
    path('all_posts/', views.PostView.as_view(), name='all_posts'),
    path('crud_form/', views.crud_form, name='crud_form'),
    path('<int:pk>', views.DetailPost.as_view(), name='detail'),
    path('<int:pk>/update', views.UpDate.as_view(), name='update'),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('', views.HomeView.as_view(), name='home'),
    
    
]


