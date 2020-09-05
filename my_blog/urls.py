from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('article/',include('article.urls',namespace='article')),

    path('userprofile/',include('userprofile.urls',namespace='userprofile')),

    path('comment/',include('comment.urls',namespace='comment')),
]

