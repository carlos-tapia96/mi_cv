from django.urls import path
from . import views


app_name = "app_blog"

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),

]
