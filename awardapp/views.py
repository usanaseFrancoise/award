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
             we also need to set
             a condition to set a user to rate 
             only once
             '''
        arrrate=[]
        for use in votes:
            arrrate.append(use.user_id)

        auth=arrrate

        reviews=ReviewForm(request.POST)
        if request.method =='POST':
            if reviews.is_valid():
                comment=reviews.save(commit=False)
                comment.user=request.user
                comment.save()
                return.redirect('projects',project_id)

            else:
                reviews=ReviewForm()

        user_comments=Comment.objects.filter(pro_id=project_id)
        context = {
        'projects':projects,
        'form':form,
        'usability':average_usability,
        'design':average_design,
        'content':average_content,
        'average_rating':average_rating,
        'auth':auth,
        'all':all,
        'average':average,
        'comments':user_comments,
        'reviews':reviews,
        
    }
    return render(request,'post.html',context)

@login_required(login_url='/accounts/login/')
def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    projects = Projects.get_profile_projects(profile.id)
    
    return render(request, 'users/profile.html',{"profile":profile,"profile_details":profile_details,"projects":projects}) 


@login_required(login_url='/accounts/login/')
def post_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('home')
    else:
        form =ProjectUploadForm()
            
    return render(request,'uploads.html',{"form":form,})




def search_results(request):
    if 'titles' in request.GET and request.GET['titles']:
        search_term = request.GET.get("titles")
        searched_projects = Project.search_by_projects(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"projects":searched_projects})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"projects":searched_projects})



                 





