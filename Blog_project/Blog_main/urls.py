from django.urls import path
from Blog_main import views
from Blog_main import views

urlpatterns = [
    path('',views.Bloglist.as_view(),name="blog_list"),
    path('write/',views.createblog.as_view(),name="create_blog"),
    path('details/<slug:slug>',views.blog_details,name="blog_details"),
    path('liked/<pk>/',views.liked,name="liked"),
    path('unliked/<pk>/',views.Unliked,name="unliked"),
    path('myblog/',views.myblog.as_view(),name="myblog"),
    path('edit/<pk>/',views.Updateview.as_view(),name="edit_block"),
    
    

    
]


