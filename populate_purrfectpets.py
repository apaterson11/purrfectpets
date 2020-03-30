import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purrfectpets.settings')

import django
django.setup()
from purrfectpets_project.models import Pet, PetPhoto, Category, Comment
from django.contrib.auth.models import User
from random import randint
from django.core.files import File

def populate():
    users = [               #list of users
        {'user':'Alex', 'email':'apaterson11.ap11@gmail.com', 'password':'password', 'first_name':'Alex', 'last_name':'Paterson'},
        {'user':'Sarah', 'email':'sarah@gmail.com', 'password':'password', 'first_name':'Sarah', 'last_name':'Paterson'},
        {'user':'Andrew', 'email':'andrew@gmail.com', 'password':'password', 'first_name':'Andrew', 'last_name':'Paterson'},
        {'user':'Jake', 'email':'jake@gmail.com', 'password':'password', 'first_name':'Jake', 'last_name':'Paterson'},
        {'user':'Joe', 'email':'joe@gmail.com', 'password':'password', 'first_name':'Joe', 'last_name':'Paterson'},
        {'user':'Beth', 'email':'beth@gmail.com', 'password':'password', 'first_name':'Beth', 'last_name':'Langlands'},
        ]
        
    for user in users:      #adds users
        add_user(user['user'], user['email'], user['password'], user['first_name'], user['last_name'])
        
    for user in User.objects.all():         #prints users
        print(user)

    #lists of dictionaries of animals
    dogs = [
        {'animalType':'DO', 'name': 'Rover', 'owner': User.objects.get(username='Beth'), 'breed': 'Shih Tzu', 'awwCount':6, 'bio':'This dog belongs to Bradley Cooper.'},
        {'animalType':'DO', 'name': 'Fido', 'owner': User.objects.get(username='Joe'), 'breed': 'Golden Labrador', 'awwCount':3, 'bio':'My wee Fido. He has gotten so big! And he is only 4 years old. Wonderful.'},
        {'animalType':'DO', 'name': 'Clifford', 'owner': User.objects.get(username='Joe'), 'breed': 'Red Labrador Retriever', 'awwCount':4, 'bio':'Blimey, he is massive.'},
        ]
    cats = [
        {'animalType':'CA', 'name': 'Tiger', 'owner': User.objects.get(username='Sarah'), 'breed': 'Tortoiseshell tabby', 'awwCount':1, 'bio':'We used to have the kitten of this cat, but it got hit by a car. Fun! Good cat.'},
        {'animalType':'CA', 'name': 'Bobo', 'owner': User.objects.get(username='Alex'), 'breed': 'Moggy', 'awwCount':3, 'bio':'The friendliest cat you will ever meet. Has no teeth!'},
        ]
    fish = [
        {'animalType':'FI', 'name': 'Nemo', 'owner': User.objects.get(username='Jake'), 'breed': 'Clown Fish', 'awwCount':2, 'bio':'He wilding.'},
        {'animalType':'FI', 'name': 'Dory', 'owner': User.objects.get(username='Beth'), 'breed': 'Pacific blue tang fish', 'awwCount':6, 'bio':'She cannot find Nemo please help her.'},
        {'animalType':'FI', 'name': 'Marlin', 'owner': User.objects.get(username='Jake'), 'breed': 'Clown Fish', 'awwCount': 3, 'bio':'Have you seen his son?'},
        {'animalType':'FI', 'name': 'Bruce', 'owner': User.objects.get(username='Alex'), 'breed': 'Great white shark', 'awwCount':0, 'bio':'He too wishes to find this fish.'},
        ]
    reptiles = [
        {'animalType':'RE', 'name': 'Harry Potter', 'owner': User.objects.get(username='Andrew'), 'breed': 'Horn tailed firewhizzer', 'awwCount':3, 'bio':'Weird.'},
        ]
    rodents = [
        {'animalType':'RO', 'name': 'Remy', 'owner': User.objects.get(username='Sarah'), 'breed': 'Rat', 'awwCount':1, 'bio':'Remy believes anyone can cook! Which is silly, for he is a rat.'},
        {'animalType':'RO', 'name': 'Brian', 'owner': User.objects.get(username='Sarah'), 'breed': 'Gerbil', 'awwCount':2, 'bio':'Our last gerbil died while we were on holiday so the people looking after him put him in our freezer. Turns out, he was still alive, but then froze to death. Unfortunate. Anyway, this is Brian. We are going on holiday soon.'},
        ]
    other = [
        ]
    
    #list of categories
    cats = {'dogs': {'name':'dogs', 'category': dogs, 'views': 128, 'animalType':'DO'},
            'cats': {'name':'cats', 'category': cats, 'views': 64, 'animalType':'CA'}, 
            'fish': {'name':'fish', 'category': fish, 'views': 32, 'animalType':'FI'},
            'reptiles': {'name':'reptiles', 'category': reptiles, 'views': 1, 'animalType':'RE'},
            'rodents': {'name':'rodents', 'category': rodents, 'views': 500, 'animalType':'RO'},
            'other': {'name':'other', 'category': other, 'views': 0, 'animalType':'OT'},
            }
    
    #the code below goes through the cats dictionary, then adds each dictionary and then adds all associated pages for that category
    
    for cat, cat_data in cats.items():       
        c = add_cat(cat_data['name'], cat_data['views'], cat_data['animalType'])      
        for p in cat_data['category']:
            add_pet(c, p['name'], p['owner'], p['breed'], p['awwCount'], p['bio'], users)
            

    # print out the categories we have added
    for c in Category.objects.all():
        for p in Pet.objects.filter(category=c):
            print(f'- {c}: {p}')
    
    #list of comments
    comments = [
        {'commentMaker':User.objects.get(username='Alex'), 'email': 'alex@gmail.com', 'timeDate':'2017-02-14', 'comment':'Nice!', 'approved':True},
        {'commentMaker':User.objects.get(username='Sarah'), 'email': 'sarah@gmail.com', 'timeDate':'2020-03-28', 'comment':'Cute dog!', 'approved':True},
        {'commentMaker':User.objects.get(username='Andrew'), 'email': 'andrew@gmail.com', 'timeDate':'2016-02-13', 'comment':'Lovely content thanks for sharing.', 'approved':True},
        {'commentMaker':User.objects.get(username='Joe'), 'email': 'joe@gmail.com', 'timeDate':'2020-02-14', 'comment':'WHere am I?', 'approved':True},
        {'commentMaker':User.objects.get(username='Jake'), 'email': 'jake@gmail.com', 'timeDate':'2020-01-29', 'comment':'AAAAAAAAAAAAAAAAAAAAAAAaa', 'approved':True},
        {'commentMaker':User.objects.get(username='Beth'), 'email': 'beth@gmail.com', 'timeDate':'2018-02-14', 'comment':'haha thanks very cool', 'approved':False},
        ]
    
    #adds all comments
    for dict in comments:
        add_comment(dict['commentMaker'], dict['email'], dict['timeDate'], dict['comment'], dict['approved']) 
    
    #prints all comments
    for comment in Comment.objects.all():
        print(comment)
    
    #creates pet photo objects
    pet_photos = [
        {'pet':Pet.objects.get(name='Rover'), 'photo': File(open("rover.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Fido'), 'photo': File(open("fido.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Clifford'), 'photo': File(open("clifford.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Tiger'), 'photo': File(open("tiger.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Bobo'), 'photo': File(open("bobo.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Nemo'), 'photo': File(open("nemo.jpg",'rb'))},
        ]
    
    #adds all pet photos
    for photo in pet_photos:
        add_pet_photo(photo['pet'], photo['photo'])
        
    #prints all photos
    for photo in PetPhoto.objects.all():
        print(photo)
        
#method that adds categories
def add_cat(name, views, animalType):
    cat = Category.objects.get_or_create(animalType=animalType)[0]
    cat.name = name
    cat.views = views
    cat.save()
    return cat
    
#method that adds pets
def add_pet(c,  name, owner, breed, awwCount, bio, users):
    p = Pet.objects.get_or_create(category=c, name=name, owner=owner)[0]
    p.breed=breed
    
    names = [li['user'] for li in users]                          #iterates through users and makes them awwSenders depending on awwCount
    if awwCount != 0:
        for i in range(0, awwCount):
            sender = User.objects.get(username=names[i])
            p.awwSenders.add(sender)
    
    p.awwSenders.add(owner)
    p.awwCount=awwCount
    p.bio=bio
    p.save()
    return p
    
#method that adds pet photos
def add_pet_photo(pet, photo):
    p_p = PetPhoto.objects.get_or_create(photo=photo)[0]
    p_p.pet=pet
    p_p.save()
    return p_p
   
#method that adds comments
def add_comment(commentMaker, email, timeDate, comment, approved):
    com = Comment.objects.get_or_create(user=commentMaker, body=comment, created = timeDate)[0]
    com.email = email
    com.approved = approved
    com.save()
    return com
 
#method that adds users 
def add_user(user, email, password, first_name, last_name):
    u = User.objects.create_user(user, email, password)
    u.first_name = first_name
    u.last_name = last_name
    u.save()
    return u
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()