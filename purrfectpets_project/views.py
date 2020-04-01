
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from purrfectpets_project.forms import UserForm, PetForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Category, Pet, PetPhoto, Comment, User
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
	pet = Pet.objects.all()
	context = {'pet': pet}
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

@login_required
def my_pets(request,username):
    
    user = User.objects.get(username = username)

    try:
        pets = Pet.objects.filter(owner = user)
    except:
        pets = None


    context_dict = {'pets':pets}

    return render(request, 'purrfectpets_project/my_pets.html', context=context_dict)
	

	
def pet_page(request, username, pet_name_slug):
    context_dict = {}

    user = User.objects.get(username=username)

    try:
        pet = Pet.objects.get(owner = user, slug = pet_name_slug)
        
        context_dict['pet'] = pet
    except:
        context_dict['pet'] = None

    try:
        photos = PetPhoto.objects.filter(pet=pet)
        context_dict['photos'] = photos
    except Exception as e:
        print(e)
        context_dict['photos'] = None

    try:
        comments = Comment.objects.filter(pet = pet)
        context_dict['comments'] = comments
    except:
        context_dict['comments'] = None
         

    print(context_dict)
    return render(request, 'purrfectpets_project/pet_page.html', context = context_dict)
	
	
#@login_required	
#def add_picture(request, pet_name_slug):
#    return  render(request, 'purrfectpets_project/add_picture.html', {'form': form})
	

@login_required
def add_pet(request):
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
                pet = form.save(commit = True)
                pet.awws = 0
                pet.owner = User.objects.get(username=request.user.username)
                #pet.category = Category.objects.get(name='dogs')
                pet.save()
                return redirect('/purrfectpets_project/my_pets/')
        else:
            print(form.errors)
    context_dict = {'form': form}
    return render(request, 'purrfectpets_project/add_pet.html', context = context_dict)


@login_required
def delete_account(request, username):
    user = get_object_or_404(User, username = username)
    if request.method == "POST":
        user.delete()
        return redirect("/purrfectpets_project/")

    context_dict = {'username':user.username}

    return render(request, "purrfectpets_project/delete_account.html", context_dict)

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

"""
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
"""

class PetList(generic.ListView):
	queryset = Pet.objects.filter(category = "DO").order_by("-created_on")
	template_name= "dogs.html"

def post_detail(request, slug):
	template_name = 'post_detail.html'
	pet = get_object_or_404(Post, slug=slug)
	comments = post.comments.order_by("-created_on")
	new_comment = None

	context = {'pet': pet}

	if request.method == "POST":
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():

			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(
		request, 
		template_name, 
		{
			"pet": pet, 
			"comments": comments, 
			"new_comment": new_comment, 
			"comment_form": comment_form,
		},
	)

"""
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
"""







