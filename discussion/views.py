from django.shortcuts import render,redirect
from .models import DiscussionPost,Type
from .forms import DiscussionForm, ResponseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def view_discussion(request):
    posts = DiscussionPost.objects.all()
    context = {'posts':posts}
    print(posts)
    return render(request, 'discussion/discussion-posts.html',context)

def single_discussion(request,pk):
    form = ResponseForm()
    post = DiscussionPost.objects.get(id = pk)
    if request.method == "POST":
        form = ResponseForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.discussion_post = post
        post.CountReview
        review.save()
        return redirect('single-discussion', pk = post.id)
    
    context = {'post':post,'form':form}
    return render(request, 'discussion/single-discussion.html', context)

def create_discussion(request):
    form = DiscussionForm()
    user = request.user.profile
    if request.method == "POST":
            newtags = request.POST.get("newtags").replace(","," ").split()
            form = DiscussionForm(request.POST,request.FILES)
            if form.is_valid():
                disc = form.save()
                disc.owner = user
                for tag in newtags:
                    tag, created = Type.objects.get_or_create(name = tag)
                    disc.tags.add(tag)
                disc.save()
            return redirect('view-discussion')
    context = {'form':form}
    return render(request,'discussion/disc-form.html',context)
