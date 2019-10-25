from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Profile,Rate,Project
from .forms import ProfileEditForm,ProjectUploadForm,VotesForm
# Create your views here.

def home(request):
    projects=Project.objects.all()
    context={
        'projects':projects,

    }
    return render(request,'index.html',context)

 def projects(request,project_id):

    try:

        projects=Project.objects.get(id=project_id)
        all=Rate.objects.filter(project=project_id)
        print(all)


    except Exception as e:

        raise Http404()
         '''
         rating
         '''
        count=0
        for i in all:

            count+=i.usability
            count+=i.design
            count+=i.content

        if count>0:
            average=round(count/3,1)

        else:
            average=0    

        if request.method =='POST':
            form=VotesForm(request.POST)
            if form.is_valid():
                rate =form.save(commit=False)
                rate.user=request.user
                rate.project=project_id
                rate.save()
            return redirect('projects',project_id)

        else:
            form=VotesForm()

        votes=Rate.objects.filter(project=project_id)
        usability=[]
        design=[]
        content=[]
        

        for i in votes:
            usability.append(i.usability)
            design.append(i.design)
            content.append(i.content)


        if len(usability)>0 or len(design)>0 or len(content)>0:
            average_usability=round(sum(usability)/len(usability),1)
            average_design=round(sum(design)/len(design),1)
            average_content=round(sum(content)/len(content),1)

            average_rating=rpund((average_usability+average_design+average_content)/3,1)


        else:
            average_usability=0.0
            average_design=0.0
            average_content=0.0
             average_rating=0.0

             '''
             we also need




