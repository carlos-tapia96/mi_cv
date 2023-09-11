from django.shortcuts import render
from django.contrib import  messages
from .forms import ContactForm
from django.views import generic




#En resumen, esta vista ContactView se utiliza para mostrar un formulario 
# de contacto en la página "contact.html". Cuando el formulario se 
# envía correctamente, se guarda y se muestra un mensaje de éxito al 
# usuario, y luego se redirige al usuario a la página de inicio.
class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def from_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you")
        return super().form_valid(form)









