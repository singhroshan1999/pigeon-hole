from django.shortcuts import render
from forum import query,forms
from django.http import HttpResponse
def index(request):
    cont_dict = {'posts':query.get_post()['post']}
    print(request.user)
    return render(request,'forum/posts.html',cont_dict)

def create_hole(request):
    if request.user.is_authenticated:
        form = forms.CreateHoleForm()
        if request.method == 'POST':
            form = forms.CreateHoleForm(request.POST)
            if form.is_valid():
                hole_stat = query.create_hole(request.user.get_username(),form.cleaned_data['hole'])
                if  not hole_stat:
                    print('hole already exist')
                else:
                    return HttpResponse("hole created")
            # AnonymusUser
        else:
            return render(request,'forum/create_hole.html',{'form':form})
    else:
        pass

def create_post(request):
    if request.user.is_authenticated:
        form = forms.CreatePostForm()
        if request.method == 'POST':
            form = forms.CreatePostForm(request.POST)
            if form.is_valid():
                query.create_post(request.user.get_username(),form.cleaned_data['hole'],form.cleaned_data['post'])
                return HttpResponse("posted")
            # AnonymusUser
        else:
            return render(request,'forum/create_post.html',{'form':form})
    else:
        pass
    
