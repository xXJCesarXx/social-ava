"""
URL configuration for social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include, re_path
from socialapp.views import index, sobre, postar,contato, new_avalia, editar_avalia, deleta_avalia
from socialapp.views import new_post, deleta_post, editar_post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('postar/', postar, name='postar'),
    path('contato/', contato, name='contato'),
    path('new_avalia/', new_avalia, name='new_avalia'),
    path('editar_avalia/<str:id>', editar_avalia, name='editar_avalia'),
    path('deleta_avalia/<int:id>', deleta_avalia, name='deleta_avalia'),
    #post
    path('new_post/', new_post, name='new_post'),
    path('editar_post/<str:id>', editar_post, name='editar_post'),
    path('deleta_post/<int:id>', deleta_post, name='deleta_post'),

    path('', include('usuario.urls')),



]
