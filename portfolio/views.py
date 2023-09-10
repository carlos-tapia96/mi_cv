from django.shortcuts import render
from django.views import generic
from .models import Portfolio

# Create your views here.
#En resumen, esta vista PortfolioView se utiliza para mostrar una lista 
# paginada de objetos del modelo Portfolio en la plantilla 
# "main/portfolio.html". Los objetos que se muestran son solo aquellos 
# que tienen is_active establecido en True. Si tienes más de 10 objetos, 
# se dividirán en páginas separadas con 10 objetos por página.

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "portfolio.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)





#En resumen, esta vista se utiliza para mostrar los detalles de un objeto 
# específico del modelo Portfolio en la plantilla "main/portfolio-detail.html".
# Es útil cuando deseas permitir a los usuarios ver los detalles completos de
# un elemento del portafolio específico en tu sitio web.
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name= "portfolio-detail.html"
