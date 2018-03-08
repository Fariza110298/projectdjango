from django.contrib import admin
from django.urls import path
from django.conf.urls import url


from teacher import views
urlpatterns = [
    path('1/', views.basic_one, name='basic_one'),
    path('2/', views.template_two, name='template_two'),
    path('3/', views.template_three_simple, name='template_three_simple'),
    path('all/', views.teachers, name='teachers'),
    path('all2/', views.students, name='students'),
]
#url(r'^articles/get/(?P<article_id>\d+)$', views.article, name='article'),