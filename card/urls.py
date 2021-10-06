from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.logout, name= 'logout'),
    path('<str:card_id>', views.carddetail, name= 'carddetail'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('editcardinfos/', views.editcard, name='editcardinfos'),

]