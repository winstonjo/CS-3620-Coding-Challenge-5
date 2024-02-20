from . import views
from django.urls import path

app_name = 'Home'

urlpatterns = [

    path('', views.index, name='index'),
    # Path for the url detail view
    path('<int:id>', views.detail, name='detail'),
    path('Hobbies/', views.hobbies, name='Hobbies'),
    path('Portfolio/', views.portfolio, name='Portfolio'),
    path('Contact/', views.contact, name='Contact')
]