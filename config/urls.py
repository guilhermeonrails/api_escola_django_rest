from django.contrib import admin
from django.urls import path, include
from escola.urls import router_urls
from escola.views import ListaMatriculasAluno, ListaAlunosMatriculados, DetalhesAlunoCurso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('aluno/<int:aluno_id>/curso/<int:curso_id>', DetalhesAlunoCurso.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
