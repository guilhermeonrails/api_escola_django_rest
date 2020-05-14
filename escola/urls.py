from rest_framework import routers
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

router_urls = router.urls