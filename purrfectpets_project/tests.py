from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from purrfectpets_project.models import Category
from purrfectpets_project import views


# Tests on views which can be accessed without calls to the models

class Test_home_view(TestCase):

    def test_list_url_accessible(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/home.html')

"""
    def test_home_with_no_most_viewed_categories(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no Categories up yet!')
        self.assertEquals(response.context['categories'], None)

"""

class test_about_us_view(TestCase):

     def test_about_us_correct_template(self):
        response = self.client.get(reverse('purrfectpets_project:about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/about_us.html')


class test_contact_us_view(TestCase):

     def test_contact_us_correct_template(self):
        response = self.client.get(reverse('purrfectpets_project:contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/contact_us.html')


class test_popular_pets_view(TestCase):

     def test_popular_pets_correct_template(self):
        response = self.client.get(reverse('purrfectpets_project:popular_pets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/popular_pets.html')



class test_register_view(TestCase):

     def test_register_correct_template(self):
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration_form.html')

class test_login_view(TestCase):

     def test_register_correct_template(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')




    


