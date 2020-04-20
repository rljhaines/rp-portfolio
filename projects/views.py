from django.shortcuts import render
from projects.models import Project
from blog.models import Post
from training_log.models import Entry


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
     project = Project.objects.get(pk=pk)
     context = {'project': project}
     if(pk==1):
         return render(request, 'project_detail.html', context)
     elif(pk==2):
         posts = Post.objects.all().order_by("-created_on")
         context = {'posts': posts}
         return render(request, 'blog_index.html', context)
     elif(pk==3):
         entry = Entry.objects.all().order_by("-created_on")
         context = {'entry': entry}
         return render(request, 'training_log.html', context)
