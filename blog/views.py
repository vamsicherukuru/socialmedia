from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from braces.views import SuperuserRequiredMixin,StaffuserRequiredMixin
from .forms import UserForm,UserProfileForm
from django.contrib.auth  import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import (BlogPostForm,BlogCommentForm,FeedbackForm,NewsPostForm,NewsCommentForm)

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

def RegisterView(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_pic_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_pic_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_pic_form.save(commit=False)
            profile.user = user
            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(profile_pic_form.errors,user_form.errors)

         
    else:
        user_form = UserForm()
        profile_pic_form = UserProfileForm()

    return render(request,'registration.html',{'user_form':user_form,'profile_pic_form':profile_pic_form
        , 'registered':registered
        })
        
########################################
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:home'))
            else:
                return HttpResponse("not active user")
        else:
            return HttpResponse("Invalid Credentials")
        
    else:
        return render(request,'login.html',{})
#################3

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))

######################################################################################


class profilePage(TemplateView):
    template_name = 'profilepage.html'



##################################
class NewsList(ListView):
    model = models.NewsPost
    context_object_name = 'news_list'
    queryset = models.NewsPost.objects.order_by('-post_date')
    template_name = 'news_list.html'

class NewsPostDetail(DetailView):

    model = models.NewsPost
    context_object_name = 'post_detail'
    template_name = 'news_detail.html'
   


class NewsNewPostView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'news_post_form.html'
    model = models.NewsPost
    fields = '__all__'
    template_name = 'news_post_form.html'
    def test_func(self):
        return self.request.user.is_staff
    


class NewsAddComment(CreateView):
    model = models.NewsComment
    template_name = 'news_comment_form.html'
    form_class = NewsCommentForm

    def form_valid(self,form):
        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('blog:news')


class AstroBlog(ListView):
    model = models.BlogPost
    context_object_name = 'post_list'
    queryset = models.BlogPost.objects.order_by('-post_date')
    template_name = 'astroblog.html'

class AstroPostDetail(DetailView):

    model = models.BlogPost
    context_object_name = 'post_detail'
    template_name = 'blog_post_detail.html'
   


class NewPostView(LoginRequiredMixin,CreateView,StaffuserRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'post_form.html'
    model = models.BlogPost
    fields = '__all__'
    template_name = 'post_form.html'
    
    


class AddComment(CreateView):
    model = models.BlogComment
    
    template_name = 'comment_form.html'
    form_class = BlogCommentForm

    def form_valid(self,form):
        

        form.instance.Post_id  = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('blog:astroblog' )



class FeedbackView(CreateView):
    model = models.Feedback
    redirect_field_name = 'feedback_form.html'
    
    fields = '__all__'
    template_name = 'feedback_form.html'