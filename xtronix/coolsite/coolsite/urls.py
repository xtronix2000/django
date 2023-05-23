"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from women.views import * #  index, categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')) #  http://10.1.2 01.58:8000/ 
    # просто добавили приложение women, оно независимо от проекта
    # все благодаря добавление файла urls.py в приложение women
]

from coolsite import settings
if settings.DEBUG:  # в режиме откладки когда дебаг тру, мы к маршрутам выше добавляем
    #  еще доин маршрут для статических данных, графических файлов 
    # сначала префикс setting.MEDIA_URL, а затем коневую папку где будут находится эти файлы
    # все это делается только в отладочном режиме
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
