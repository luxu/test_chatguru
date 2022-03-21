from django.contrib import admin

from backend.models import Planeta, Filme


class PlanetaAdmin(admin.ModelAdmin):
    ...


class FilmeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Planeta, PlanetaAdmin)
admin.site.register(Filme, FilmeAdmin)
