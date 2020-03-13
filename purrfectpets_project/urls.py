from django.contrib import admin
from django.urls import path
from django.urls import include
from purrfectpets_project import views
from django.conf import settings

app_name = 'purrfectpets'

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('popular_pets/', views.popular_pets, name="popular_pets"),
    path('categories/', views.categories, name="categories"),
    path('dogs/', views.dogs, name="dogs"),
    path('cats/', views.cats, name="cats"),
    path('fish/', views.fish, name="fish"),
    path('reptiles/', views.reptiles, name="reptiles"),
    path('rodents/', views.rodents, name="rodents"),
    path('other/', views.other, name="other"),
    path('sign_up/', views.sign_up, name='sign_up'), 
	path('login/', views.user_login, name='login'),
	path('login/my_account', views.my_account name='my_account'),
	path('login/my_account/my_pets', views.my_pets name='my_pets'),
	path('login/my_account/my_pets/<slug:pet_name>/', views.pet_page, name = 'pet_page'),
	path('login/my_account/my_pets/<slug:pet_name>/add_picture/', views.add_picture, name = 'add_picture'),
	path('login/my_account/add_pet/', views.add_pet, name = 'add_pet'),
	path('restricted/', views.restricted, name='restricted'),
	path('logout/', views.user_logout, name = 'logout'),
]