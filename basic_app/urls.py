from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'basic_app' 

urlpatterns = [
      
    path('', views.home.as_view(), name='home'),  
    path('recipies', views.postlist.as_view(), name='recipies'),  
    path('detail/<int:pk>/', views.postdetail.as_view(), name='detail'),
    path('recipies/detail/<int:pk>/', views.postdetail.as_view(), name='detail'),
    path('explore', views.randomlist.as_view(), name='randomlist'),  
    path('Contact', views.contact.as_view(), name='contact'),
    # path('About', views.about.as_view(), name='about'),
    path('ingredients', views.ingredients_list.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.ingredients_detail.as_view(), name='ingdetail'),
    path('search/', views.search, name='search'),
    path('search/detail/<int:pk>', views.postdetail.as_view(), name='detailse'),
    # path('starlist/<int:pk>/', views.stardetail.as_view(), name='stardetail'),
    # path('starlist/<int:x>/detail<int:pk>/', views.basicdetail.as_view(), name='detail'),
    # path('channel/', views.channellist.as_view(), name='channellist'),
    # path('channel/detail/<int:pk>/', views.channeletail.as_view(), name='channeldetail'),
    # path('channel/detail/<int:x>/detail<int:pk>/', views.basicdetail.as_view(), name='detail'),

 
]     