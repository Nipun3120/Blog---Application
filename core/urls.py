from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path(r'<slug:slug>/$', views.blogView, name='blog'),
    path('new-blog/', views.createBlogView, name='createBlog'),
    path(r'edit-blog/<slug:slug>', views.editBlogView, name='editBlog'),
    path(r'delete-blog/<slug:slug>', views.deleteBlogView, name='deleteBlog'),
    # path(r'blog/delete/<slug:slug>', views.deleteConfirm, name='delete'),
    path(r'like/<slug:slug>', views.likeBlog, name='blog_like')
]

