from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
import insta_app

urlpatterns= [
    path('', views.home, name='home'),
    re_path(r'^search/', views.search_results, name='search_results')
    path('<int:image_id>'/,views.image,name='image'),
    re_path(r'register/', views.register_request,name='register'),
    re_path(r'login/', views.login_request, name='login'),
    re_path(r'logout/', views.logout_request, name='logout'),
    path('like/<id>', views.like, name='like'),
    path('image/<id>', views.comment, name='comment'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)