from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Initiate login procedure using OpenID
    path('login', views.login, name='login'),

    # Initiate logout procedure
    path('logout', views.logout, name='logout'),

    # Once the user has authenticated using OpenID, they are re-routed back to this URL
    path('authenticated', views.authenticated, name='authenticated'),

    # Initiate `client_credentials` based flow URL
    path('authorize/client-credentials', views.authorize_via_client_credentials,
         name="authorize-via-client-credentials"),

    # Initiate `authorization_code` based flow URL
    path('authorize/authorization-code', views.authorize_via_authorization_code,
         name="authorize-via-authorization-code"),

    # Once the user has been authorized, they are re-routed to this URL
    path('auth-code-authorized', views.auth_code_authorized, name='auth-code-authorized')
]
