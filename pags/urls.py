from django.urls import path
from .views import HomPag

urlpatterns = [
    path('', HomPag.as_view(), name='home'),
]