
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from purrfectpets_project.forms import UserForm, PetForm, EditAccountForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Category, Pet, PetPhoto, Comment, User
from django.views import generic, View
from .forms import CommentForm, PetPhotoForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.utils.decorators import method_decorator


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
    context_dict = {}
    pet_list = Pet.objects.order_by('-awwCount')[:10]
    context_dict['pets'] = pet_list
    
#    user=User.objects.get(username=username)
    
    
#    try:
#        pet=Pet.objects.get(owner = user, slug = pet_name)
#        context_dict['pet']=pet
#    except:
#        context_dict['pet'] = None 
#    try:
#        photos = PetPhoto.objects.filter(pet=pet)[:1]
#        context_dict['photos']=photos
#    except Exception as e:
#        print(e)
#        context_dict['photos'] = None 
        
    return render(request, 'purrfectpets_project/popular_pets.html', context=context_dict)
	
def categories(request):
	context_dict = {}
	return render(request, 'purrfectpets_project/categories.html', context=context_dict)
	
def dogs(request):
    context_dict = {}
    category = Category.objects.get(animalType='DO')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list

    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/dogs.html', context=context_dict)
    return response

	
def cats(request):
    context_dict = {}
    category = Category.objects.get(animalType='CA')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/cats.html', context=context_dict)
    return response
	
def fish(request):
    context_dict = {}
    category = Category.objects.get(animalType='FI')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/fish.html', context=context_dict)
    return response
	
def rodents(request):
    context_dict = {}
    category = Category.objects.get(animalType='RO')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/rodents.html', context=context_dict)
    return response

def reptiles(request):
    context_dict = {}
    category = Category.objects.get(animalType='RE')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/reptiles.html', context=context_dict)
    return response
	
def other(request):
    context_dict = {}
    category = Category.objects.get(animalType='OT')
    pet_list = Pet.objects.filter(category=category)
    context_dict['pets'] = pet_list
    
    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    # Return response back to the user, updating any cookies that need changed.
    category.views += 1
    category.save()
    response = render(request, 'purrfectpets_project/other.html', context=context_dict)
    return response

@login_required
def my_account(request):
    return render(request, 'purrfectpets_project/my_account.html')


@login_required
def my_pets(request,username):
	context_dict = {}
	try:
		owner = User.objects.get(username = username)
		pets = Pet.objects.filter(owner = owner)
		context_dict['pets'] = pets
	except Pet.DoesNotExist:
		context_dict['pets'] = None
	return render(request, 'purrfectpets_project/my_pets.html', context = context_dict)
	

	
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

    context_dict['admirers'] = pet.awwSenders.all()
    print(context_dict)         
    return render(request, 'purrfectpets_project/pet_page.html', context = context_dict)


class awwPet(View):

    @method_decorator(login_required)
    def get(self, request):
        pet_id = request.GET['pet_id']
        user_id = request.GET['user_id']
        try:
            pet = Pet.objects.get(id=int(pet_id))
            
        except Pet.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
            
        pet.awwCount = pet.awwCount + 1
        pet.awwSenders.add(User.objects.get(id=int(user_id)))

        pet.save()
        
        return HttpResponse(pet.awwCount)

class disAwwPet(View):

    @method_decorator(login_required)
    def get(self, request):
        pet_id = request.GET['pet_id']
        user_id = request.GET['user_id']
        try:
            pet = Pet.objects.get(id=int(pet_id))
            
        except Pet.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
            
        pet.awwCount = pet.awwCount - 1
        pet.awwSenders.remove(User.objects.get(id=int(user_id)))

        pet.save()
        
        return HttpResponse(pet.awwCount)
	
	
#@login_required	
#def add_picture(request, pet_name_slug):
#    return  render(request, 'purrfectpets_project/add_picture.html', {'form': form})
	

@login_required
def add_pet(request):
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
                pet = form.save(commit = False)
                pet.awws = 0
                pet.owner = User.objects.get(username=request.user.username)
                pet.save()
                p_p = PetPhoto.objects.get_or_create(photo=request.FILES.get("photos"))[0]
                p_p.pet=pet
                p_p.save()
                return redirect('/purrfectpets_project/my_pets/' + request.user.username)
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'purrfectpets_project/add_pet.html', context = context_dict)
    
@login_required
def add_photo(request, username, pet_name_slug):
    form = PetPhotoForm()

    owner = User.objects.get(username=username)

    pet = Pet.objects.get(owner = owner, slug = pet_name_slug)

    if request.method == 'POST':
        print(request.FILES)
        form = PetPhotoForm(request.POST)
        photo = request.FILES.get("photo")
        if photo:
            p_p = PetPhoto.objects.get_or_create(photo=request.FILES.get("photo"))[0]
            p_p.pet=pet
            p_p.save()
            return redirect('/purrfectpets_project/pet_page/'+owner.username+"/"+pet.slug+"/")  
        else:
            print(form.errors)
    

    context_dict = {'form': form, 'pet':pet}
    return render(request, 'purrfectpets_project/add_photo.html', context_dict)


@login_required
def delete_pet(request, username, pet_name_slug):
    owner = User.objects.get(username=username)
    pet = Pet.objects.get(owner = owner, slug = pet_name_slug)
    
    if request.method == "POST":
        pet.delete()
        return redirect("/purrfectpets_project/my_pets/" + owner.username)

    context_dict = {'pet':pet}

    return render(request, "purrfectpets_project/delete_pet.html", context_dict)

@login_required
def edit_account(request):
    if request.method == "POST":
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            return redirect('/purrfectpets_project/my_account/')
        else:
            return redirect('/purrfectpets_project/edit_account')
    else:
        form = EditAccountForm(instance=request.user)
        args = {'form': form}
        return render(request, 'purrfectpets_project/edit_account.html', args)
    
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/purrfectpets_project/my_account/')
        else:
            messages.error(request, "Error, please try again!")
            return redirect('/purrfectpets_project/edit_account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'purrfectpets_project/change_password.html', args)
    
	
@login_required
def add_comment(request, username, pet_name_slug):
    form = CommentForm()

    owner = User.objects.get(username=username)

    pet = Pet.objects.get(owner = owner, slug = pet_name_slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = User.objects.get(username=request.user.username) 
            comment.pet = pet
            comment.save()
            return redirect('/purrfectpets_project/pet_page/'+owner.username+"/"+pet.slug+"/")  
        else:
            print(form.errors)
    

    context_dict = {'form': form, 'pet':pet}
    return render(request, 'purrfectpets_project/add_comment.html', context_dict)


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


class PetList(generic.ListView):
	queryset = Pet.objects.filter(category = "DO").order_by("-created_on")
	template_name= "dogs.html"


def visitor_cookie_handler(request):
    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, then the default value of 1 is used.
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    visits = visits + 1
    request.session['last_visit'] = str(datetime.now())

    request.session['visits'] = visits
        
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val
    







