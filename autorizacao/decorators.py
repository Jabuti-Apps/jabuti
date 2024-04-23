from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def gestor_required(view_func):
    """
    Decorator que verifica se o usuário tem a função de gestor.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'G':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return _wrapped_view

def motorista_required(view_func):
    """
    Decorator que verifica se o usuário tem a função de motorista.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'M':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return _wrapped_view

def funcionario_required(view_func):
    """
    Decorator que verifica se o usuário tem a função de funcionário.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 'F':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return _wrapped_view
