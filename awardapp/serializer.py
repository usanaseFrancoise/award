from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_photo',) 
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image_landing','link')