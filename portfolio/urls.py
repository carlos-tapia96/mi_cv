from django.urls import path
from . import views


app_name = "app_portfolio"

urlpatterns = [
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    

]
