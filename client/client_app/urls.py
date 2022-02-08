from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('authenticated', views.authenticated, name='authenticated'),
    path('authorize/client-credentials', views.authorize_via_client_credentials,
         name="authorize-via-client-credentials"),
    path('authorize/authorization-code', views.authorize_via_authorization_code,
         name="authorize-via-authorization-code"),
    path('auth-code-authorized', views.auth_code_authorized, name='auth-code-authorized')
]
