from django.urls import path 
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.blog_list, name = "blog_list"),
    path("<int:blog_id>/", blog_views.get_blog_by_id, name ="blog_details"),
    path('author/<int:author_id>/', blog_views.blog_by_author, name='blog_by_author'),
]