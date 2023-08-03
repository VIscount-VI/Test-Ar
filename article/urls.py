from django.urls import path
from .views import ArtecilList, CreateView





urlpatterns = [
    path('', ArtecilList.as_view(), name="list"),
    path('add/', CreateView.as_view(), name='creat_list'),
]