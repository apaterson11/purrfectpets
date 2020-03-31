
from django.contrib import admin
from django.urls import path
from django.urls import include
from purrfectpets_project import views
from django.conf import settings
from django.conf.urls import url


app_name = 'purrfectpets_project'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('about_us/', views.about_us, name="about_us"),
    path('popular_pets/', views.popular_pets, name="popular_pets"),
    path('categories/', views.categories, name="categories"),
    #path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('dogs/', views.dogs, name="dogs"),
    path('cats/', views.cats, name="cats"),
    path('fish/', views.fish, name="fish"),
    path('reptiles/', views.reptiles, name="reptiles"),
    path('rodents/', views.rodents, name="rodents"),
    path('other/', views.other, name="other"),
    #path('sign_up/', views.sign_up, name='sign_up'), 
	#path('login/', views.user_login, name='login'),
	path('my_account/', views.my_account, name='my_account'),
	path('my_pets/', views.my_pets, name='my_pets'),
	path('login/my_account/my_pets/<slug:pet_name>/', views.pet_page, name = 'pet_page'),
	path('login/my_account/my_pets/<slug:pet_name>/add_picture/', views.add_picture, name = 'add_picture'),
	path('login/my_account/add_pet/', views.add_pet, name = 'add_pet'),
	path('logout/', views.user_logout, name = 'logout'),
    path('delete_account/<int:user_id>/', views.delete_account, name='delete_account')

    #url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    #url(r'^templates/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    #url(r'^$', views.list_of_post, name='list_of_post')
    #url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment')
]