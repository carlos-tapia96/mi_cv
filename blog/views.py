from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.

#En resumen, esta vista BlogView se utiliza para mostrar una lista 
# paginada de entradas de blog (objetos del modelo Blog) en la plantilla
# "main/blog.html". Los objetos que se muestran son solo aquellos que
# tienen is_active establecido en True. Si tienes más de 10 entradas de
# blog, se dividirán en páginas separadas con 10 entradas por página.
class BlogView(generic.ListView):
    model = Blog
    template_name = "blog.html"
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)



