from django import forms
from .models import Profile,Project,Rate


class ProjectUpForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title','image_landing','description','link')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_photo','bio','website')

class VotesForm(forms.ModelForm):
    class Meta:
        model=Rate
        field=('design','usability','content')


