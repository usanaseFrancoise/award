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
          
        self.image = Project(title = 'leaves')
        self.image.save_projects()


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Project))
 

    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_projects()
        images = Project.objects.all()
        self.assertTrue(len(images)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
       
        Project.objects.all().delete()



class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='fanny')
        self.profile = Profile.objects.create(user = self.user,bio = 'say something', phone_number= 788494207)

    
    
    
     def test_save_method(self):
            '''
            test profile by save
            '''
            self.nature.save_profile()
            comm = Profile.objects.all()
            self.assertTrue(len(comm)>0) 
    

class CommentTestClass(TestCase):

    def setUp(self):
     
        self.user1 = User(username='fanny')
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()

        self.james=Project(2,title='James',description='beautiful',user=self.user1,likes="1",post="image")
        self.james.save_image()
        self.com=Comment(comment='leaves',comment_image=self.james,posted_by=self.nature,)
        self.com.save_com()

 
    def test_instance(self):

        self.assertTrue(isinstance(self.com,Comment))    
       
    def test_save_method(self):
        '''
        test image by save
        '''
        self.com.save_com()
        comm=Comment.objects.all()
        self.assertTrue(len(comm)>0)