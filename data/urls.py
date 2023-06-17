from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Aboutme', views.Aboutme, name='Aboutme'),
    path('Refference', views.Refference, name='Refference'),
    path('Aboutstory', views.Aboutstory, name='Aboutstory'),
    path('Chinesehistory', views.Chinesehistory, name='Chinesehistory'),
    path('Chinesebuilding', views.Chinesebuilding, name='Chinesebuilding'),
    path('Era1', views.Era1, name='Era1'),
    path('Era2', views.Era2, name='Era2'),
    path('Era3', views.Era3, name='Era3'),
    path('Culture', views.Culture, name='Culture'),
    path('Map', views.Map, name='Map'),
    path('Video', views.Video, name='Video'),
    path('Story', views.Story, name='Story'),
    path('Upload', views.Upload, name='Upload'),
]