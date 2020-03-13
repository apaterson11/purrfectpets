from django.urls import path
from purrfect_pets import views

app_name = 'purrfect_pets'

urlpatterns = [
	path('home/', views.home, name = 'home'),
	path('about_us/', views.about_us, name = 'about_us'),
	path('contact_us/', views.contact_us, name = 'contact_us'),
	path('popular_pets/', views.popular_pets name ='popular_pets'),
	path('categories/', views.categories, name = 'categories'),
	path('categories/dog/', views.dog, name = 'dog'),
	path('categories/cat/', views.cat, name = 'cat'),
	path('categories/fish/', views.fish, name = 'fish'),
	path('categories/rodent/', views.rodent, name = 'rodent'),
	path('categories/other/', views.other, name = 'other'),
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