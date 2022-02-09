from django.urls import path, include

urlpatterns = [
    path('client_app/', include('client_app.urls')),
]
