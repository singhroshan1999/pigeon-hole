from django.shortcuts import render,redirect
from forum import query,forms
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import random
def index(request):
    post = query.get_post(request,end = 20)
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
                kwarg = {}
                # print(request.POST)
                if 'hole_pic' in request.FILES:
                    fileName = request.FILES['hole_pic'].name
                    request.FILES['hole_pic'].name = str(random.randint(1,10000)*random.randint(1,10000)) + fileName[fileName.rfind('.'):]
                    kwarg['hole_pic'] =  request.FILES['hole_pic']
                    # hole_pic = request.FILES['hole_pic']
                hole_stat = query.create_hole(request.user.get_username(),form.cleaned_data['hole'],form.cleaned_data['hole_description'],**kwarg)
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
                kwarg = {}
                if 'image' in request.FILES:
                    fileName = request.FILES['image'].name
                    request.FILES['image'].name = str(random.randint(1,10000)*random.randint(1,10000)) + fileName[fileName.rfind('.'):]
                    kwarg['image'] =  request.FILES['image']
                query.create_post(request.user.get_username(),form.cleaned_data['hole'],form.cleaned_data['post'],form.cleaned_data['title'],**kwarg)
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

# @login_required
def set_vote(request,is_up,pk):
    if is_up == 'up':
        up = True
    elif is_up == 'down':
        up = False
    resp = query.set_vote_by_pk(request,up,pk)
    if resp == 0:
        # return HttpResponse("voted")
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse("error")


def get_post_tree(request,pk):
    # con_dict = {}
    reply_tree = query.get_reply_tree_by_pk(pk)
    print(reply_tree)
    # post = Post.objects.get(pk = pk)
    post_data = query.get_post(request,pk = pk)['post'][0]
    print(post_data)
    # print('-=-=-=-=-=-=--=')
    return render(request,'forum/post_main.html',{'post':post_data[0],
                                                  'count':post_data[1],
                                                  'is_up':post_data[2],
                                                  'reply':reply_tree,
                                                  'verbose':reply_tree
                                                  }
                  )
def set_reply(request,pk):
    if request.method == 'POST':
        form = forms.CreateReplyForm(request.POST)
        if form.is_valid():
            if query.set_reply_by_pk(request,pk,form.cleaned_data['reply']) == 0:

                return redirect(query.get_parent_post(pk))
            else:
                return HttpResponse('error in setting reply')
        else:
            return HttpResponse('form invalid')
    else:
        form = forms.CreateReplyForm()
        return render(request,'forum/reply.html',{'form':form})