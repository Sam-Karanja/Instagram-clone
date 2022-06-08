from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
import insta_app

urlpatterns= [
    path('', views.home, name='home'),
    re_path(r'^search/', views.search_results, name='search_results')
    path('<int:image_id>'/,views.image,name='image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)