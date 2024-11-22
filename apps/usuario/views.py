from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout
from .forms import RegistroUsuarioForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from .forms import UsuarioUpdateForm
from django.urls import reverse_lazy

# Create your views here.

class Logueo(LoginView):
    template_name = "registration/login.html"

    def form_invalid(self, form):
        """No es obligatorio sobreescribir este método, pero es útil para agregar mensajes de error personalizados."""
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        print("Error")
        return super().form_invalid(form)

class RegistroUsuario(FormView):
    template_name = 'html/registro.html'
    form_class = RegistroUsuarioForm 
    success_url = reverse_lazy('perfil') 

    def form_valid(self, form):
        user = form.save()
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

@login_required
def editar_cuenta(request):
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UsuarioUpdateForm(instance=request.user)

    return render(request, 'html/editar_cuenta.html', {'form': form})