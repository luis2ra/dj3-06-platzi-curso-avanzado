"""Main URLs module."""

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

'''
esto es una prueba pa verificar el docker de django que
se ejecuta por separado

1. se mata la instancia de docker de django
$ docker rm -f <ID>

2. se levanta en otra consola la imagen de django
$ docker-compose -f local.yml run --rm --service-ports django

'''
# import pdb; pdb.set_trace()

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
