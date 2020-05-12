from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'ativo')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'alunos', 'cursos', 'periodo')
    list_display_links = ('id',)
    search_fields = ('alunos',)
    list_filter = ('periodo',)
    list_editable = ('periodo',)
    list_per_page = 10

admin.site.register(Matricula, Matriculas)