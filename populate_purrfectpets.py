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
        {'user':'pet_lover99', 'email':'pet_lover99@gmail.com', 'password':'password', 'first_name':'Alex', 'last_name':'Paterson'},
        {'user':'john_smith_1964', 'email':'john_smith_1964@gmail.com', 'password':'password', 'first_name':'John', 'last_name':'Smith'},
        {'user':'dandyandy', 'email':'andrew@gmail.com', 'password':'password', 'first_name':'Andrew', 'last_name':'Paterson'},
        {'user':'surfergal62', 'email':'jake@gmail.com', 'password':'password', 'first_name':'Jake', 'last_name':'Paterson'},
        {'user':'samsepi0l', 'email':'elliot@gmail.com', 'password':'password', 'first_name':'Elliot', 'last_name':'Alderson'},
        {'user':'1whoknox', 'email':'bb@gmail.com', 'password':'password', 'first_name':'Heisen', 'last_name':'Berg'},
        ]
        
    for user in users:      #adds users
        add_user(user['user'], user['email'], user['password'], user['first_name'], user['last_name'])
        
    for user in User.objects.all():         #prints users
        print(user)

    #lists of dictionaries of animals
    fish = [
        {'animalType':'FI', 'name': 'Nemo', 'owner': User.objects.get(username='surfergal62'), 'breed': 'Clown Fish', 'awwCount':2, 'bio':'He wilding.', 'created_on':'2020-03-29'},
        {'animalType':'FI', 'name': 'Dory', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Pacific blue tang fish', 'awwCount':6, 'bio':'She cannot find Nemo please help her.', 'created_on':'2020-03-29'},
        {'animalType':'FI', 'name': 'Marlin', 'owner': User.objects.get(username='surfergal62'), 'breed': 'Clown Fish', 'awwCount': 3, 'bio':'Have you seen his son?', 'created_on':'2020-03-29'},
        {'animalType':'FI', 'name': 'Bruce', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Great white shark', 'awwCount':0, 'bio':'He too wishes to find this fish.', 'created_on':'2020-03-29'},
        ]
    dogs = [
        {'animalType':'DO', 'name': 'Rover', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Mongrel', 'awwCount':6, 'bio':'This dog belongs to Bradley Cooper.', 'created_on':'2017-02-14'},
        {'animalType':'DO', 'name': 'Fido', 'owner': User.objects.get(username='samsepi0l'), 'breed': 'Golden Labrador', 'awwCount':3, 'bio':'My wee Fido. He has gotten so big! And he is only 4 years old. Wonderful.', 'created_on':'2020-02-14'},
        {'animalType':'DO', 'name': 'Clifford', 'owner': User.objects.get(username='samsepi0l'), 'breed': 'Red Labrador Retriever', 'awwCount':2, 'bio':'Blimey, he is massive.', 'created_on':'2020-04-01'},
        {'animalType':'DO', 'name': 'Jack-Russell', 'owner': User.objects.get(username='dandyandy'), 'breed': 'Jack Russell', 'awwCount':3, 'bio':'His name is Jack Russell. And he is a Jack Russell. Haha!', 'created_on':'2020-04-01'},
        {'animalType':'DO', 'name': 'Poppy', 'owner': User.objects.get(username='1whoknox'), 'breed': 'Old English Sheepdog', 'awwCount':4, 'bio':'From Shetland!', 'created_on':'2020-04-01'},
        {'animalType':'DO', 'name': 'Kiwi', 'owner': User.objects.get(username='surfergal62'), 'breed': 'Labradoodle', 'awwCount':4, 'bio':'I am really bored of typing these bios now.', 'created_on':'2020-04-01'},
        ]
    cats = [
        {'animalType':'CA', 'name': 'Lizzie', 'owner': User.objects.get(username='john_smith_1964'), 'breed': 'Tortoiseshell tabby', 'awwCount':1, 'bio':'We used to have the kitten of this cat, but it got hit by a car. Fun! Good cat.', 'created_on':'2020-03-14'},
        {'animalType':'CA', 'name': 'Maisey', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Moggy', 'awwCount':3, 'bio':'The friendliest cat you will ever meet. Has no teeth!', 'created_on':'2020-03-29'},
        {'animalType':'CA', 'name': 'Ziggy', 'owner': User.objects.get(username='surfergal62'), 'breed': 'Siamese', 'awwCount':2, 'bio':'If you please.', 'created_on':'2020-03-29'},
        {'animalType':'CA', 'name': 'Snaps', 'owner': User.objects.get(username='surfergal62'), 'breed': 'Ginger tabby', 'awwCount':4, 'bio':'Used to live across the road from me. I miss him!', 'created_on':'2020-03-29'},
        ]
    reptiles = [
        {'animalType':'RE', 'name': 'Harry Potter', 'owner': User.objects.get(username='dandyandy'), 'breed': 'Horn tailed firewhizzer', 'awwCount':3, 'bio':'Weird.', 'created_on':'2020-03-29'},
        {'animalType':'RE', 'name': 'Paarthurnax', 'owner': User.objects.get(username='1whoknox'), 'breed': 'Komodo dragon', 'awwCount':2, 'bio':'You should avoid hurting this lizard. He is cool.', 'created_on':'2020-03-29'},
        {'animalType':'RE', 'name': 'Kaa', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Rock Python', 'awwCount':0, 'bio':'Do NOT look him in the eyes.', 'created_on':'2020-03-29'},
        ]
    rodents = [
        {'animalType':'RO', 'name': 'Remy', 'owner': User.objects.get(username='dandyandy'), 'breed': 'Rat', 'awwCount':1, 'bio':'Remy believes anyone can cook! Which is silly, he is a rat.', 'created_on':'2020-03-29'},
        {'animalType':'RO', 'name': 'Brian', 'owner': User.objects.get(username='pet_lover99'), 'breed': 'Gerbil', 'awwCount':2, 'bio':'Our last gerbil died while we were on holiday so the people looking after him put him in our freezer. Turns out, he was still alive, but then froze to death. Unfortunate. Anyway, this is Brian. We are going on holiday soon.', 'created_on':'2020-03-29'},
        ]
    other = [
        ]
    
    #list of categories
    cats = {'dogs': {'name':'dogs', 'category': dogs, 'views': 500, 'animalType':'DO'},
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
            add_pet(c, p['name'], p['owner'], p['breed'], p['awwCount'], p['bio'], p['created_on'], users)
            

    # print out the categories we have added
    for c in Category.objects.all():
        for p in Pet.objects.filter(category=c):
            print(f'- {c}: {p}')
    
    #list of comments
    comments = [
        {'pet':Pet.objects.get(name='Rover'), 'name':User.objects.get(username='pet_lover99'), 'created_on':'2017-02-14', 'body':'Nice!', 'active':True},
        {'pet':Pet.objects.get(name='Rover'), 'name':User.objects.get(username='1whoknox'), 'created_on':'2017-02-14', 'body':'He is beautiful!', 'active':True},
        {'pet':Pet.objects.get(name='Fido'), 'name':User.objects.get(username='john_smith_1964'), 'created_on':'2020-03-28', 'body':'Cute dog!', 'active':True},
        {'pet':Pet.objects.get(name='Clifford'), 'name':User.objects.get(username='dandyandy'), 'created_on':'2016-02-13', 'body':'Lovely content thanks for sharing.', 'active':True},
        {'pet':Pet.objects.get(name='Lizzie'), 'name':User.objects.get(username='samsepi0l'), 'created_on':'2020-02-14', 'body':'WHere am I?', 'active':True},
        {'pet':Pet.objects.get(name='Maisey'), 'name':User.objects.get(username='surfergal62'), 'created_on':'2020-01-29', 'body':'AAAAAAAAAAAAAAAAAAAAAAAaa', 'active':True},
        {'pet':Pet.objects.get(name='Nemo'), 'name':User.objects.get(username='1whoknox'), 'created_on':'2018-02-14', 'body':'haha thanks very cool', 'active':False},
        ]
    
    #adds all comments
    for dict in comments:
        add_comment(dict['pet'], dict['name'], dict['created_on'], dict['body'], dict['active']) 
    
    #prints all comments
    for comment in Comment.objects.all():
        print(comment)
    
    #creates pet photo objects
    pet_photos = [
        {'pet':Pet.objects.get(name='Rover'), 'photo': File(open("rover.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Fido'), 'photo': File(open("fido.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Clifford'), 'photo': File(open("clifford.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Lizzie'), 'photo': File(open("lizzie.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Maisey'), 'photo': File(open("maisey.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Jack-Russell'), 'photo': File(open("jack-russell.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Poppy'), 'photo': File(open("poppy.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Kiwi'), 'photo': File(open("kiwi.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Ziggy'), 'photo': File(open("ziggy.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Snaps'), 'photo': File(open("snaps.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Paarthurnax'), 'photo': File(open("paarthurnax.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Harry Potter'), 'photo': File(open("harrypotter.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Kaa'), 'photo': File(open("kaa.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Remy'), 'photo': File(open("remy.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Brian'), 'photo': File(open("brian.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Nemo'), 'photo': File(open("nemo.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Dory'), 'photo': File(open("dory.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Marlin'), 'photo': File(open("marlin.jpg",'rb'))},
        {'pet':Pet.objects.get(name='Bruce'), 'photo': File(open("bruce.jpg",'rb'))},
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
def add_pet(c,  name, owner, breed, awwCount, bio, created_on, users):
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
    p.created_on = created_on
    p.save()
    return p
    
#method that adds pet photos
def add_pet_photo(pet, photo):
    p_p = PetPhoto.objects.get_or_create(photo=photo)[0]
    p_p.pet=pet
    p_p.save()
    return p_p
   
#method that adds comments
def add_comment(pet, name, created_on, body, active):
    com = Comment.objects.get_or_create(pet=pet, name=name, body=body, created_on = created_on)[0]
    com.active = active
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
    print('Starting Purrfect Pets population script...')
    populate()