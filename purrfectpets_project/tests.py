from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from purrfectpets_project.models import Category
from purrfectpets_project.views import home
import os
import importlib
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}!!Test Failed!! =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class General_set_up_test(TestCase):
    """
    Simple tests to probe the file structure of the project currently.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.app_dir = os.path.join(self.project_base_dir, 'purrfectpets_project')
    
    def test_project_created(self):
        """
        Tests whether the purrfectpets configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'purrfectpets'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'purrfectpets', 'urls.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Purrfectpets configuration directory doesn't exist{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}Project's urls.py module does not exist{FAILURE_FOOTER}")
    
    def test_app_created(self):
        """
        Determines whether the Purrfectpets app has been created.
        """
        directory_exists = os.path.isdir(self.app_dir)
        is_python_package = os.path.isfile(os.path.join(self.app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.app_dir, 'views.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The purrfectpets app directory does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The purrfectpets app directory is missing files{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The purrfectpets app directory is missing files{FAILURE_FOOTER}")
    
    def test_app_has_urls_module(self):

        module_exists = os.path.isfile(os.path.join(self.app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The purrfectpets app's urls.py module is missing{FAILURE_FOOTER}")
    
    def test_is_purrfectpets_project_app_configured(self):
        """
        Is the new purrfectpets app in INSTALLED_APPS list?
        """
        is_app_configured = 'purrfectpets_project' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The purrfectpets app is missing from setting's INSTALLED_APPS list.{FAILURE_FOOTER}")


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

     def test_categories_correct_template(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/categories.html')
"""
class Test_pet_views(TestCase):

    def test_list_url_accessible(self):
        response = self.client.get(reverse('dogs'))
        self.assertEquals(response.status_code, 200)

    def test_dog_correct_template(self):
        response = self.client.get(reverse('dogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purrfectpets_project/dogs.html')
    


