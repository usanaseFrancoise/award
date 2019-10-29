from django.test import TestCase
from .models import Project,User,Profile,Comments
import datetime as dt


class ProjectTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='fanny')
        self.user1.save()
          
        self.image = Project(title = 'leaves',description = 'beautiful',user=self.user1,project_image = "image")
        self.image.save_projects()


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))
