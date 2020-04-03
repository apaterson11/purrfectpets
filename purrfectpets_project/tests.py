from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from purrfectpets_project.models import Category
from purrfectpets_project.views import home



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

"""
class test_categories_view(TestCase):

     def test_home_correct_template(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/categories.html')
"""
    


