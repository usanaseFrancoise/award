from django import forms
from .models import Profile,Project,Rate,Comments


class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','image_landing', 'link')
        
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','website') 
        
class VotesForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('design','usability','content')
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments',)
        