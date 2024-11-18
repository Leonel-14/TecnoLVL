from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout
from .forms import RegistroUsuarioForm
from django.views.generic.edit import FormView


# Create your views here.

class Logueo(LoginView):
    template_name = "registration/login.html"

    def form_invalid(self, form):
        """No es obligatorio sobreescribir este método, pero es útil para agregar mensajes de error personalizados."""
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        print("Errorr")
        return super().form_invalid(form)

class RegistroUsuario(FormView):
    template_name = 'html/registro.html'
    form_class = RegistroUsuarioForm  # Asocia el formulario correcto
    success_url = 'perfil/'  # Redirige después del registro exitoso

    def form_valid(self, form):
        user = form.save()  # Guarda el usuario
        login(self.request, user)  # Autentica y crea la sesión
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
class Perfil(TemplateView):
    template_name = 'html/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["usuario"] = self.request.user
        return context


def exit(request):
    logout(request)
    return redirect('inicio')

