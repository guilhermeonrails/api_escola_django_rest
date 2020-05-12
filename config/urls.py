from django.contrib import admin
from django.urls import path, include
from escola.urls import router_urls
from escola.views import ListaMatriculasAluno, ListaAlunosMatriculados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_urls)),
    path('lista/matriculas/aluno/<int:pk>/', ListaMatriculasAluno.as_view()),
    path('lista/matriculas/curso/<int:pk>/', ListaAlunosMatriculados.as_view()),
]
