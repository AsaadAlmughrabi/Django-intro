from django.test import TestCase,SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomeTest(SimpleTestCase):
    def test_home_page_status_code(self):
        url=reverse('Home')
        response = self.client.get(url)
        self.assertEqual(response.status_code ,200)

    def test_home_page(self):
        url= reverse("Home")
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')


class AboutTest(SimpleTestCase):
    def test_about_page_status_code(self):
        url=reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code ,200)

    def test_about_page(self):
        url=reverse('about')
        res=self.client.get(url)
        self.assertTemplateUsed(res,'About.html')

class ContactTest(SimpleTestCase):
    def test_contact_page_status_code(self):
        url=reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code ,200)

    def test_contact_page(self):
        url=reverse('contactUs')
        res=self.client.get(url)
        self.assertTemplateUsed(res,'contactUs.html')

    
