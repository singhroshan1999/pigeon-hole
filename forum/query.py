from forum.models import Hole,Post,HoleFollower,PostVoteCount
from authentication.models import UserPortfolio
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_post(request,start = 0,end = 10,user = None,hole = None,pk = None):
    post = {}
    if user is None and hole is None and pk is None:
        post['post'] = Post.objects.filter(reply_id = 0).order_by('-creation_datetime')[start:end]
    elif user is not None and hole is not None:
        if User.objects.filter(username = user).exists() and Hole.objects.filter(hole = hole).exists():
            user = User.objects.filter(username = user)[0]
            hole = Hole.objects.get(hole = hole)
            post['post'] = Post.objects.filter(reply_id = 0,user = user,hole = hole).order_by('-creation_datetime')[start:end]
    elif user is not None:
        if User.objects.filter(username = user).exists():
            user = User.objects.filter(username = user)[0]
            post['post'] = Post.objects.filter(reply_id = 0,user = user).order_by('-creation_datetime')[start:end]
    elif hole is not None:
        if Hole.objects.filter(hole = hole).exists():
            hole = Hole.objects.get(hole = hole)
            post['post'] = Post.objects.filter(reply_id = 0,hole = hole).order_by('-creation_datetime')[start:end]
    elif pk is not None:
        if Post.objects.filter(pk = pk).exists():
            post['post'] = [Post.objects.get(pk = pk)]
            
    count = []
    is_voted = []
    if User.objects.filter(username = request.user.get_username()).exists():
        auth_user = User.objects.get(username = request.user.get_username())
    else:
        auth_user = None
    post_new = {'post':[]}
    for i in post['post']:
        if PostVoteCount.objects.filter(post = i,user = auth_user).exists():
            v = PostVoteCount.objects.get(post = i,user = auth_user).is_up
        else:
            v = None
        post_new['post'].append([i,
                                 PostVoteCount.objects.filter(post = i,is_up = True).count() - PostVoteCount.objects.filter(post = i,is_up = False).count(),
                                 v])
        # count.append(PostVoteCount.objects.filter(post = i).count())
        # is_voted.append(PostVoteCount.objects.filter(post = i,user = auth_user))
    # post['votes'] = count[:]
    # post['is_voted'] = is_voted[:]
    # print(post)
    return post_new

def get_hole(start = 0,end = 10,user = None,order_by_modified = True):
    hole = {}
    if order_by_modified:
        order = '-modified_date'
    else:
        order = '-creation_date'
        
    if user is None:
        hole['hole'] = Hole.objects.order_by(order)[start:end]
    elif user is not None:
         if User.objects.filter(username = user).exists():
            user = User.objects.get(username = user)
            hole['hole'] = Hole.objects.filter(user = user).order_by(order)[start:end]
    return hole

def get_user(start = 0,end = 10):
    return UserPortfolio.objects.all()[start:end]

# @login_required
def create_hole(username,hole,description,**kwarg):
    if Hole.objects.filter(hole = hole).exists() == False:
        user = User.objects.get(username = username)
        h = Hole.objects.create(user = user,hole = hole,hole_description = description,**kwarg)
        h.save()
        return True
    else:
        return False
            # already exist

def create_post(username,hole,post,title,**kwarg):
    if Hole.objects.filter(hole = hole).exists() == False:
        create_hole(username,hole)
    h = Hole.objects.get(hole = hole)
    user = User.objects.get(username = username)
    p = Post.objects.create(user = user,hole = h,post = post,title = title,**kwarg)
    p.save()

# def get_profile(username)

def get_hole_by_name(hole):
    if Hole.objects.filter(hole = hole).exists() == True:
        return Hole.objects.get(hole = hole)
    else:
        pass # hole dont exists    

def get_user_by_username(username):
    if User.objects.filter(username = username).exists():
        return User.objects.get(username = username)
    else:
        pass # user dont exist

# def get_votes_by_post_pk(pk): # list
# #     votes = PostVoteCount.objects
# def get_all_post_info(request,)

def set_vote_by_pk(request,up,pk):
    # truth_table = [None,True]
    if Post.objects.filter(pk = pk).exists():
        user = User.objects.get(username = request.user.get_username())
        post = Post.objects.get(pk = pk)
        if PostVoteCount.objects.filter(user = user,post = post).exists():
            vote = PostVoteCount.objects.get(user = user,post = post)
            # vote.is_up = truth_table[up^vote.is_up]&up
            # print('-=-=-=-=-=-=-=-=-=-=-=-=')
            if vote.is_up == up:
                vote.delete()
            else:
                vote.is_up = not vote.is_up
                vote.save()

        else:
            PostVoteCount.objects.create(user = user,post = post,is_up = up)
        return 0
    else:
        return 1

def get_reply_tree_by_pk(pk):
    # post = Post.objects.get(pk = pk)
    reply_list = Post.objects.filter(reply_id = pk).order_by('-creation_datetime')
    reply_all = []
    for reply in reply_list:
        curr_reply = [reply]
        curr_reply.append(Post.objects.filter(reply_id = reply.pk).order_by('-creation_datetime'))
        reply_all.append(curr_reply)
    return reply_all

def set_reply_by_pk(request,pk,post):
    if Post.objects.filter(pk = pk).exists():
        Post.objects.create(
            user = User.objects.get(username = request.user.get_username()),
            hole = get_hole_by_name('holehole'),
            title = '',
            post = post,
            reply_id = pk
        )
        return 0
    return 1

def get_parent_post(pk):
    
    post_redir = Post.objects.get(pk = pk)
    if post_redir.reply_id != 0:
        post_redir = Post.objects.get(pk = post_redir.reply_id)
    return '/forum/post/'+str(post_redir.pk)