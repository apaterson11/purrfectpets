
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
#from purrfectpets_project import Category, Page
#from purrfectpets_project import CategoryForm, PageForm
#from purrfectpets_project.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from datetime import datetime

def home(request):
	context_dict = {}	
	#context_dict['categories'] = category_list
	#context_dict['pages'] = page_list
	return render(request, 'purrfectpets/home.html', context=context_dict)

def about_us(request):
	context_dict = {}
	return render(request, 'purrfectpets/about_us.html', context=context_dict)
	
def contact_us(request):
	context_dict = {}
	return render(request, 'purrfectpets/contact_us.html', context=context_dict)
	
def popular_pets(request):
	context_dict = {}
	return render(request, 'purrfectpets/popular_pets.html', context=context_dict)
	
def categories(request):
	context_dict = {}
	return render(request, 'purrfectpets/categories.html', context=context_dict)
	
def dogs(request):
	context_dict = {}
	return render(request, 'purrfectpets/dogs.html', context=context_dict)
	
def cats(request):
	context_dict = {}
	return render(request, 'purrfectpets/cats.html', context=context_dict)
	
def fish(request):
	context_dict = {}
	return render(request, 'purrfectpets/fish.html', context=context_dict)
	
def rodents(request):
	
	context_dict = {}
	return render(request, 'purrfectpets/rodents.html', context=context_dict)

def reptiles(request):
    return render(request, 'purrfectpets/reptiles.html')
	
def other(request):
	context_dict = {}
	return render(request, 'purrfectpets/other.html', context=context_dict)

@login_required
def my_account(request):
    return render(request, 'purrfectpets/my_account.html')

def my_pets(request):
    return render(request, 'purrfectpets/my_pets.html')
	

	

@login_required
def pet_page(request, pet_name_slug):
    context_dict = {}
    try:
        category = Pet.objects.get(slug = pet_name_slug)
        
        context_dict['pet'] = pet
    except pet.DoesNotExist:
        context_dict['pet'] = None
       
    return render(request, 'purrfectpets/pet_page.html', context = context_dict)

@login_required	
def add_category(request):
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
	
		if form.is_valid():
			form.save(commit=True)
			return redirect('/rango/')
		else:
			print(form.errors)
	return render(request, 'rango/add_category.html', {'form': form})
	
	
@login_required	
def add_picture(request, pet_name_slug):
    return  render(request, 'purrfectpets/add_picture.html', {'form': form})
	

@login_required
def add_pet(request):
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/purrfect_pets/')

    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            if category:
                pet = form.save(commit = False)
                pet.category = category
                pet.awws = 0
                page.save()
                return redirect(reverse('purrfectpets:pet_page', kwargs = {'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'purrfectpets/add_pet.html', context = context_dict)

"""
def sign_up(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'purrfectpets/sign_up.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
"""
def sign_up(request):
    return render(request, 'purrfectpets/sign_up.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('purrfect_pets:home'))
            else:
                return HttpResponse("Your Purrfect Pets account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'purrfectpets/login.html')

@login_required 
def restricted(request): 
	return render(request, 'purrfectpets/restricted.html')

@login_required 
def user_logout(request): 
	logout(request) 
	return redirect(reverse('purrfectpets/home.html'))

