from django.urls import path,re_path
from . import views

urlpatterns = [
    path('api',views.NLP.as_view(),name="api"),
    path('models',views.Models.as_view(),name="models")
]
