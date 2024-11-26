from blog import views
from django.urls import path

app_name ='blog'

urlpatterns = [
    path('', views.index, name='index' ),
    path('page/', views.page, name='page' ),
    path('page/post/', views.post, name='post' ), 
]
