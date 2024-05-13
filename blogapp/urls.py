from django.urls import path,include
from blogapp import views
urlpatterns=[
    path('',views.home_view),
    path('signup/',views.signup_view,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('articles/', views.article_list, name='viewarticles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('addarticle/', views.submit_article, name='addarticle'),
    path('logout/',views.logout_view,name='logout'),
]
