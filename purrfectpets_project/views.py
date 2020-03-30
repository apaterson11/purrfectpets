
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from purrfectpets_project.forms import UserForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Post, Category, Pet, PetPhoto, Comment
from django.views import generic
from .forms import CommentForm


def home(request):
    context_dict = {}	
    category_list = Category.objects.order_by('-views')[:3]
    pet_list = Pet.objects.order_by('-awwCount')[:3]
    context_dict['categories'] = category_list
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/home.html', context=context_dict)

def about_us(request):
	context_dict = {}
	return render(request, 'purrfectpets_project/about_us.html', context=context_dict)
	
def contact_us(request):
	context_dict = {}
	return render(request, 'purrfectpets_project/contact_us.html', context=context_dict)
	
def popular_pets(request):
	post = Post.objects.all()
	context = {'post': post}
	return render(request, 'purrfectpets_project/popular_pets.html', context)
	
def categories(request):
	context_dict = {}
	return render(request, 'purrfectpets_project/categories.html', context=context_dict)
	
def dogs(request):
    context_dict = {}
    category = Category.objects.get(animalType='DO')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/dogs.html', context=context_dict)
	
def cats(request):
    context_dict = {}
    category = Category.objects.get(animalType='CA')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/cats.html', context=context_dict)
	
def fish(request):
    context_dict = {}
    category = Category.objects.get(animalType='FI')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/fish.html', context=context_dict)
	
def rodents(request):
    context_dict = {}
    category = Category.objects.get(animalType='RO')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/rodents.html', context=context_dict)

def reptiles(request):
    context_dict = {}
    category = Category.objects.get(animalType='RE')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/reptiles.html', context=context_dict)
	
def other(request):
    context_dict = {}
    category = Category.objects.get(animalType='OT')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    return render(request, 'purrfectpets_project/other.html', context=context_dict)

@login_required
def my_account(request):
    return render(request, 'purrfectpets_project/my_account.html')

def my_pets(request):
    return render(request, 'purrfectpets_project/my_pets.html')
	

	

@login_required
def pet_page(request, pet_name_slug):
    context_dict = {}
    try:
        pet = Pet.objects.get(slug = pet_name_slug)
        
        context_dict['pet'] = pet
    except pet.DoesNotExist:
        context_dict['pet'] = None
       
    return render(request, 'purrfectpets_project/pet_page.html', context = context_dict)
	
	
@login_required	
def add_picture(request, pet_name_slug):
    return  render(request, 'purrfectpets_project/add_picture.html', {'form': form})
	

@login_required
def add_pet(request):
    try:
        pet = Pet.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/purrfectpets_project/')

    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            if category:
                pet = form.save(commit = False)
                pet.category = category
                pet.awws = 0
                page.save()
                return redirect(reverse('purrfectpets_project:pet_page', kwargs = {'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'purrfectpets/add_pet.html', context = context_dict)

def show_category(request, category_name_slug):
    context_dict = {} #create a context dictionary whch we can pass to the template rendering engine
    try: #attempt to find a category name slug with the given name
        category = Category.objects.get(slug=category_name_slug)
        
        pets = Pet.objects.filter(category=category)  #retrieve all associated pages, filter() will return a list of page objects or an empty list
        
        context_dict['pets'] = pets  #add results list to template context under pages
        context_dict['category'] = category     #and under category
    
    except Category.DoesNotExist: #if try fails, display no category message
        context_dict['category'] = None
        context_dict['pets'] = None
    
    return render(request, 'purrfectpets_project/categories.html', context=context_dict)

def sign_up(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	return render(request, 'purrfectpets_project/sign_up.html', context = {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('purrfectpets_project:my_account'))
            else:
                return HttpResponse("Your Purrfect Pets account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'purrfectpets_project/login.html')


@login_required 
def user_logout(request): 
	logout(request) 
	return redirect(reverse('purrfectpets_project:home'))


def list_of_post_by_category(request, category_slug):
	categories = Category.objects.all()
	post = Post.objects.filter(status=1)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		post = post.filter(category=category)

	context = {'categories': categories, 'post': post, 'category': category}

	return render(request, 'purrfectpets_project/list_of_post_by_category.html', context)

	
def list_of_post(request):
	post = Post.objects.filter(status=1)
	context = {'post': post}
	return render(request, 'purrfectpets_project/list_of_post.html', context)

def post_detail(request, slug):

	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'purrfectpets_project/post_detail.html', context)

def add_comment(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post 
			comment.save()
			return redirect('purrfectpets_project:post_detail', slug=post.slug)
	else:
		form = CommentForm()

	template = 'purrfectpets_project/add_comment.html'
	context = {'form': form}
	return render(request, template, context)







