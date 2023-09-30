from django.contrib import admin
from . import models


@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome', 'idade','email','contato')
    list_filter=('nome',)
    search_fields = ('nome','idade')                           
    list_per_page=10
    # list_editable=('idade','contato')
# Register your models here.
