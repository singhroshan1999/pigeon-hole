from django.shortcuts import render
from forum import query,forms
from django.http import HttpResponse
def index(request):
    post = query.get_post(request,end = 50)
    cont_dict = {'posts':post['post'],
                 'holes':query.get_hole()['hole'],
                 'users':query.get_user(),
                #  'votes':post['votes'],
                #  'is_voted':post['is_voted']
                 }
    print(request.user)
    print(cont_dict)
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
    
def temp(request):
    return render(request,'index.html')

def get_hole(request,slug):
    h = query.get_hole_by_name(slug)
    if h is not None:
        # post = query.get_post(request,end = 50,hole = h)
        # cont_dict = {'posts':post['post'],
        #             'holes':query.get_hole()['hole'],
        #             'users':query.get_user(),
        #             # 'votes':post['votes'],
        #             # 'is_voted':post['is_voted']
        #             }
        cont_dict = {'posts':query.get_post(request,end = 50,hole = h)['post'],'hole':h}
        return render(request,'forum/holes.html',cont_dict)
    else:
        return HttpResponse("hole dont exist")
    
def get_user(request,slug):
    u = query.get_user_by_username(slug)
    if u is not None:
        # post = query.get_post(request,end = 50,user = u)
        # cont_dict = {'posts':post['post'],
        #             'holes':query.get_hole()['hole'],
        #             'get_user':u,
        #             # 'votes':post['votes'],
        #             # 'is_voted':post['is_voted']
        #             }
        cont_dict = {'posts':query.get_post(request,end = 50,user = u)['post'],'get_user':u}
        return render(request,'forum/users.html',cont_dict)
    else:
        return HttpResponse("user dont exist")