"""
URL configuration for sito project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ricette import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ricetta/<int:ricetta_id>/', views.dettaglio_ricetta, name='dettaglio_ricetta'),
    path('preferiti/', views.preferiti, name='preferiti'),
    path('aggiungi/<int:ricetta_id>/', views.aggiungi_preferito, name='aggiungi_preferito'),
    path('login/', views.login_register, name='login_register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('concorrente/<int:concorrente_id>/', views.ricette_concorrente, name='ricette_concorrente'),
    path('chef/<int:chef_id>/', views.ricette_chef, name='ricette_chef'),
    path('rimuovi/<int:ricetta_id>/', views.elimina_preferito, name='elimina_preferito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
