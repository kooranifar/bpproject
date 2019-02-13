from django.urls import path, re_path
from django.contrib import admin
from . import views
from django.views.generic.base import RedirectView


app_name = 'fileuploader'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('sharedphotos/', views.sharedphotos, name = 'sharedphotos'),
    path('editphoto/', views.editphoto, name = 'editphoto'),
    path('editphoto/upload/', views.upload, name = 'upload'),
    path('myadmin/', views.myadmin, name = 'myadmin'),
    path('myadmin/auth/', views.auth, name = 'auth'),
    path('myadmin/auth/trueadmin/', views.trueadmin, name = 'trueadmin'),
    re_path(r'^myadmin/auth/trueadmin/album/(?P<album_id>[0-9]+)/$', views.adminalbum, name = 'adminalbum'),
    re_path(r'^myadmin/auth/trueadmin/album/(?P<album_id>[0-9]+)/delete/$', views.delete, name = 'delete'),

]
