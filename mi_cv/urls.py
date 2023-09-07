from django.urls import path
from . import views


app_name = "mi_cv"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),

]
