from django import forms
from blog.models import (UserProfile,BlogPost,BlogComment,Feedback, NewsPost,NewsComment)
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profilePic',)
class BlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = '__all__'

class BlogCommentForm(forms.ModelForm):
    class Meta():
        model = BlogComment
        fields = ('commentor_name','comment_text')
class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields = '__all__'
    
class NewsPostForm(forms.ModelForm):
    class Meta():
        model = NewsPost
        fields = '__all__'

class NewsCommentForm(forms.ModelForm):
    class Meta():
        model = NewsComment
        fields = ('commentor_name','comment_text')
        
