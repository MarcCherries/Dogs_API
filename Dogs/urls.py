from django.urls import path
from . import views


urlpatterns =[
    path('', views.dogs_list),
    path('<int:pk>', views.dog_detail)

]