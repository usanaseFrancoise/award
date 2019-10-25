from django.test import TestCase
from .models import Profile,Project


class ProfileTestClass(TestCase):
    def setUp(self):
        self.fanny = Profile( profile_photo='default.jpg',bio='hello', website='www.usanase.me', phone_number='788494207')

    def test_instance(self):
        self.assertTrue(isinstance(self.fanny,Profile))

    def test_save(self):
        self.fanny.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)