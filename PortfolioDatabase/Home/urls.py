from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('hobby_detail/<int:hobby_id>/', views.hobby_detail, name='hobby_detail'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
]
