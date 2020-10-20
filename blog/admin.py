from django.contrib import admin
from blog.models import (UserProfile,BlogPost,BlogComment,Feedback,NewsComment,NewsPost)

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(BlogComment)
admin.site.register(BlogPost)
admin.site.register(NewsPost)
admin.site.register(NewsComment)
admin.site.register(Feedback)