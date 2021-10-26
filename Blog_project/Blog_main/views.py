from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DetailView,View
from Blog_main.models import Blog,Likes,Comment
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Blog_main import forms
import uuid





''''
def index(request):
    return render(request,'blog_list.html',context={})'''


class myblog(LoginRequiredMixin,TemplateView):
    template_name="my_blog.html"







class createblog(LoginRequiredMixin,CreateView):
    model=Blog
    template_name='create_blog.html'
    fields=('blog_title','blog_content','blog_image',)


    def form_valid(self,form):
        blog_obj=form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('abc'))


class Bloglist(ListView):
    context_object_name='blogs'
    model=Blog
    template_name='blog_list.html'



@login_required
def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    comment_form=forms.Commentfrom()
    already_like=Likes.objects.filter(blog=blog,user=request.user)
    if already_like:
        liked=True
    else:
        liked=False    
    if request.method=='POST':
        comment_form=forms.Commentfrom(request.POST)
        if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.user=request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_details',
            kwargs={'slug':slug}))


    return render(request,'blog_details.html',context={'blog':blog,'comment':comment_form,'liked':liked})



@login_required
def liked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)
    if not already_liked:
    
        liked_post=Likes(blog=blog,user=user)
        liked_post.save()
        return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))



@login_required
def Unliked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'slug':blog.slug}))


class Updateview(LoginRequiredMixin,UpdateView):
    model=Blog
    fields=('blog_title','blog_content','blog_image',)
    template_name="edit_blog.html"


    def get_success_url(self,**kwargs):
        return reverse_lazy('blog_details', kwargs={'slug':self.object.slug})
       