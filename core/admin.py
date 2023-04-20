from django.contrib import admin
from core.models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pessoa, PessoaAdmin)
